#!/usr/bin/env python3
"""Aplica os 45 áudios PT-BR V7 sobre uma cópia original de SOUND-0.DAT.
Não sobrescreve o arquivo de origem. Gera SOUND-0_PTBR_V7.DAT na pasta indicada.
"""
from pathlib import Path
import argparse, hashlib, json, sys

ROOT = Path(__file__).resolve().parent
MANIFEST = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))

def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser(description="Aplicador do patch de áudio Theme Hospital PT-BR V7")
    ap.add_argument("original", help="caminho para o SOUND-0.DAT original")
    ap.add_argument("-o", "--output", default="SOUND-0_PTBR_V7.DAT", help="arquivo de saída (padrão: SOUND-0_PTBR_V7.DAT)")
    args = ap.parse_args()
    src = Path(args.original).expanduser().resolve()
    dst = Path(args.output).expanduser().resolve()
    if not src.is_file():
        sys.exit(f"Arquivo original não encontrado: {src}")
    if src == dst:
        sys.exit("A saída não pode ser o próprio arquivo original. Escolha outro nome/caminho.")
    if dst.exists():
        sys.exit(f"A saída já existe; não será sobrescrita: {dst}")
    if src.stat().st_size != MANIFEST["expected_size"]:
        sys.exit(f"Tamanho inesperado: {src.stat().st_size} bytes. Esperado: {MANIFEST['expected_size']}.")
    actual_hash = sha256(src)
    if actual_hash.lower() != MANIFEST["expected_sha256"].lower():
        sys.exit("O SHA-256 não corresponde ao SOUND-0.DAT original de referência. Nada foi alterado.")
    data = bytearray(src.read_bytes())
    for item in MANIFEST["clips"]:
        wav = (ROOT / item["file"]).read_bytes()
        if len(wav) != item["wav_size"] or len(wav) > item["slot_size"]:
            sys.exit(f"Clip {item['clip']}: tamanho do WAV inválido para o espaço reservado.")
        off = item["offset"]
        if data[off:off+4] != b"RIFF":
            sys.exit(f"Clip {item['clip']}: assinatura RIFF ausente no offset esperado.")
        data[off:off+item["slot_size"]] = wav + bytes(item["slot_size"]-len(wav))
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(data)
    print(f"Arquivo criado: {dst}")
    print(f"Tamanho: {len(data)} bytes")
    print(f"Clips aplicados: {len(MANIFEST['clips'])}")
    print("O original foi mantido intacto.")

if __name__ == "__main__":
    main()
