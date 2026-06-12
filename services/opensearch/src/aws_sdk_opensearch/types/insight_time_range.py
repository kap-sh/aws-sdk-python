"""Generated from Smithy shape ``com.amazonaws.opensearch#InsightTimeRange``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.long

InsightTimeRange = TypedDict(
    "InsightTimeRange",
    {
        "from": "aws_sdk_opensearch.types.long.Long",
        "to": "aws_sdk_opensearch.types.long.Long",
    },
)


# --- restJson1 ser/de ---
def serialize_json(value: InsightTimeRange) -> dict:
    out: dict = {}
    out["From"] = value["from"]
    out["To"] = value["to"]
    return out


def deserialize_json(data: dict) -> InsightTimeRange:
    out: InsightTimeRange = {}  # type: ignore[typeddict-item]
    if "From" in data:
        out["from"] = data["From"]
    else:
        raise DeserializationError("InsightTimeRange.from required")
    if "To" in data:
        out["to"] = data["To"]
    else:
        raise DeserializationError("InsightTimeRange.to required")
    return out
