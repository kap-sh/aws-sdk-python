"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#KeyModesOfUse``."""

from typing_extensions import TypedDict


class KeyModesOfUse(TypedDict, closed=True):
    encrypt: "bool"
    """<p>Speciﬁes whether an Amazon Web Services Payment Cryptography key can be used to encrypt data.</p>"""
    decrypt: "bool"
    """<p>Speciﬁes whether an Amazon Web Services Payment Cryptography key can be used to decrypt data.</p>"""
    wrap: "bool"
    """<p>Speciﬁes whether an Amazon Web Services Payment Cryptography key can be used to wrap other keys.</p>"""
    unwrap: "bool"
    """<p>Speciﬁes whether an Amazon Web Services Payment Cryptography key can be used to unwrap other keys.</p>"""
    generate: "bool"
    """<p>Speciﬁes whether an Amazon Web Services Payment Cryptography key can be used to generate and verify other card and PIN verification keys.</p>"""
    sign: "bool"
    """<p>Speciﬁes whether an Amazon Web Services Payment Cryptography key can be used for signing.</p>"""
    verify: "bool"
    """<p>Speciﬁes whether an Amazon Web Services Payment Cryptography key can be used to verify signatures.</p>"""
    derive_key: "bool"
    """<p>Speciﬁes whether an Amazon Web Services Payment Cryptography key can be used to derive new keys.</p>"""
    no_restrictions: "bool"
    """<p>Speciﬁes whether an Amazon Web Services Payment Cryptography key has no special restrictions other than the restrictions implied by <code>KeyUsage</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KeyModesOfUse) -> dict:
    out: dict = {}
    out["Encrypt"] = value.get("encrypt", False)
    out["Decrypt"] = value.get("decrypt", False)
    out["Wrap"] = value.get("wrap", False)
    out["Unwrap"] = value.get("unwrap", False)
    out["Generate"] = value.get("generate", False)
    out["Sign"] = value.get("sign", False)
    out["Verify"] = value.get("verify", False)
    out["DeriveKey"] = value.get("derive_key", False)
    out["NoRestrictions"] = value.get("no_restrictions", False)
    return out


def deserialize_aws_json_1_0(data: dict) -> KeyModesOfUse:
    out: KeyModesOfUse = {}  # type: ignore[typeddict-item]
    if "Encrypt" in data:
        out["encrypt"] = data["Encrypt"]
    else:
        out["encrypt"] = False
    if "Decrypt" in data:
        out["decrypt"] = data["Decrypt"]
    else:
        out["decrypt"] = False
    if "Wrap" in data:
        out["wrap"] = data["Wrap"]
    else:
        out["wrap"] = False
    if "Unwrap" in data:
        out["unwrap"] = data["Unwrap"]
    else:
        out["unwrap"] = False
    if "Generate" in data:
        out["generate"] = data["Generate"]
    else:
        out["generate"] = False
    if "Sign" in data:
        out["sign"] = data["Sign"]
    else:
        out["sign"] = False
    if "Verify" in data:
        out["verify"] = data["Verify"]
    else:
        out["verify"] = False
    if "DeriveKey" in data:
        out["derive_key"] = data["DeriveKey"]
    else:
        out["derive_key"] = False
    if "NoRestrictions" in data:
        out["no_restrictions"] = data["NoRestrictions"]
    else:
        out["no_restrictions"] = False
    return out
