"""Generated from Smithy shape ``com.amazonaws.securityhub#PortRangeFromTo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer

PortRangeFromTo = TypedDict(
    "PortRangeFromTo",
    {
        "from": NotRequired["aws_sdk_securityhub.types.integer.Integer"],
        "to": NotRequired["aws_sdk_securityhub.types.integer.Integer"],
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: PortRangeFromTo) -> dict:
    out: dict = {}
    if "from" in value:
        out["From"] = value["from"]
    if "to" in value:
        out["To"] = value["to"]
    return out


def deserialize_json(data: dict) -> PortRangeFromTo:
    out: PortRangeFromTo = {}  # type: ignore[typeddict-item]
    if "From" in data:
        out["from"] = data["From"]
    if "To" in data:
        out["to"] = data["To"]
    return out
