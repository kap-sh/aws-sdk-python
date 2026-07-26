"""Generated from Smithy shape ``com.amazonaws.signer#SignatureValidityPeriod``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signer.types.integer
    import capo_signer.types.validity_type


class SignatureValidityPeriod(TypedDict, closed=True):
    value: "capo_signer.types.integer.Integer"
    """<p>The numerical value of the time unit for signature validity.</p>"""
    type: NotRequired["capo_signer.types.validity_type.ValidityType"]
    """<p>The time unit for signature validity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SignatureValidityPeriod) -> dict:
    out: dict = {}
    out["value"] = value.get("value", 0)
    if "type" in value:
        import capo_signer.types.validity_type

        out["type"] = capo_signer.types.validity_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> SignatureValidityPeriod:
    out: SignatureValidityPeriod = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    else:
        out["value"] = 0
    if "type" in data:
        import capo_signer.types.validity_type

        out["type"] = capo_signer.types.validity_type.deserialize_json(data["type"])
    return out
