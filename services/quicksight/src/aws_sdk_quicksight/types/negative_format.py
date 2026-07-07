"""Generated from Smithy shape ``com.amazonaws.quicksight#NegativeFormat``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.limited_string


class NegativeFormat(TypedDict, closed=True):
    prefix: NotRequired["aws_sdk_quicksight.types.limited_string.LimitedString"]
    """<p>The prefix for a negative format.</p>"""
    suffix: NotRequired["aws_sdk_quicksight.types.limited_string.LimitedString"]
    """<p>The suffix for a negative format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NegativeFormat) -> dict:
    out: dict = {}
    if "prefix" in value:
        out["Prefix"] = value["prefix"]
    if "suffix" in value:
        out["Suffix"] = value["suffix"]
    return out


def deserialize_json(data: dict) -> NegativeFormat:
    out: NegativeFormat = {}  # type: ignore[typeddict-item]
    if "Prefix" in data:
        out["prefix"] = data["Prefix"]
    if "Suffix" in data:
        out["suffix"] = data["Suffix"]
    return out
