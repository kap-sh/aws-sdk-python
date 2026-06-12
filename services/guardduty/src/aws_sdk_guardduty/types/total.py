"""Generated from Smithy shape ``com.amazonaws.guardduty#Total``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string


class Total(TypedDict):
    amount: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The total usage.</p>"""
    unit: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The currency unit that the amount is given in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Total) -> dict:
    out: dict = {}
    if "amount" in value:
        out["amount"] = value["amount"]
    if "unit" in value:
        out["unit"] = value["unit"]
    return out


def deserialize_json(data: dict) -> Total:
    out: Total = {}  # type: ignore[typeddict-item]
    if "amount" in data:
        out["amount"] = data["amount"]
    if "unit" in data:
        out["unit"] = data["unit"]
    return out
