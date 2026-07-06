"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#KeyUsageFlags``."""

from typing_extensions import NotRequired, TypedDict


class KeyUsageFlags(TypedDict, closed=True):
    digital_signature: NotRequired["bool"]
    """<p>The digitalSignature is asserted when the subject public key is used for verifying digital signatures.</p>"""
    non_repudiation: NotRequired["bool"]
    """<p>NonRepudiation is asserted when the subject public key is used to verify digital signatures.</p>"""
    key_encipherment: NotRequired["bool"]
    """<p>KeyEncipherment is asserted when the subject public key is used for enciphering private or secret keys, i.e., for key transport.</p>"""
    data_encipherment: NotRequired["bool"]
    """<p>DataEncipherment is asserted when the subject public key is used for directly enciphering raw user data without the use of an intermediate symmetric cipher.</p>"""
    key_agreement: NotRequired["bool"]
    """<p>KeyAgreement is asserted when the subject public key is used for key agreement.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KeyUsageFlags) -> dict:
    out: dict = {}
    if "digital_signature" in value:
        out["DigitalSignature"] = value["digital_signature"]
    if "non_repudiation" in value:
        out["NonRepudiation"] = value["non_repudiation"]
    if "key_encipherment" in value:
        out["KeyEncipherment"] = value["key_encipherment"]
    if "data_encipherment" in value:
        out["DataEncipherment"] = value["data_encipherment"]
    if "key_agreement" in value:
        out["KeyAgreement"] = value["key_agreement"]
    return out


def deserialize_json(data: dict) -> KeyUsageFlags:
    out: KeyUsageFlags = {}  # type: ignore[typeddict-item]
    if "DigitalSignature" in data:
        out["digital_signature"] = data["DigitalSignature"]
    if "NonRepudiation" in data:
        out["non_repudiation"] = data["NonRepudiation"]
    if "KeyEncipherment" in data:
        out["key_encipherment"] = data["KeyEncipherment"]
    if "DataEncipherment" in data:
        out["data_encipherment"] = data["DataEncipherment"]
    if "KeyAgreement" in data:
        out["key_agreement"] = data["KeyAgreement"]
    return out
