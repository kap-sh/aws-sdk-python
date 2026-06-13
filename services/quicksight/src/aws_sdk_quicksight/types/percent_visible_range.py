"""Generated from Smithy shape ``com.amazonaws.quicksight#PercentVisibleRange``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.percent_number

PercentVisibleRange = TypedDict(
    "PercentVisibleRange",
    {
        "from": NotRequired["aws_sdk_quicksight.types.percent_number.PercentNumber"],
        "to": NotRequired["aws_sdk_quicksight.types.percent_number.PercentNumber"],
    },
)


# --- restJson1 ser/de ---
def serialize_json(value: PercentVisibleRange) -> dict:
    out: dict = {}
    if "from" in value:
        out["From"] = value["from"]
    if "to" in value:
        out["To"] = value["to"]
    return out


def deserialize_json(data: dict) -> PercentVisibleRange:
    out: PercentVisibleRange = {}  # type: ignore[typeddict-item]
    if "From" in data:
        out["from"] = data["From"]
    if "To" in data:
        out["to"] = data["To"]
    return out
