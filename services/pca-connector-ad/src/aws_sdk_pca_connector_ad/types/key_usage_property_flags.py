"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#KeyUsagePropertyFlags``."""

from typing_extensions import NotRequired, TypedDict


class KeyUsagePropertyFlags(TypedDict, closed=True):
    decrypt: NotRequired["bool"]
    """<p>Allows key for encryption and decryption.</p>"""
    key_agreement: NotRequired["bool"]
    """<p>Allows key exchange without encryption.</p>"""
    sign: NotRequired["bool"]
    """<p>Allow key use for digital signature.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KeyUsagePropertyFlags) -> dict:
    out: dict = {}
    if "decrypt" in value:
        out["Decrypt"] = value["decrypt"]
    if "key_agreement" in value:
        out["KeyAgreement"] = value["key_agreement"]
    if "sign" in value:
        out["Sign"] = value["sign"]
    return out


def deserialize_json(data: dict) -> KeyUsagePropertyFlags:
    out: KeyUsagePropertyFlags = {}  # type: ignore[typeddict-item]
    if "Decrypt" in data:
        out["decrypt"] = data["Decrypt"]
    if "KeyAgreement" in data:
        out["key_agreement"] = data["KeyAgreement"]
    if "Sign" in data:
        out["sign"] = data["Sign"]
    return out
