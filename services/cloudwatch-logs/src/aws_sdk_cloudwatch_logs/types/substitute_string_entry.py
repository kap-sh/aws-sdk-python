"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#SubstituteStringEntry``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.from_key
    import aws_sdk_cloudwatch_logs.types.source
    import aws_sdk_cloudwatch_logs.types.to_key

SubstituteStringEntry = TypedDict(
    "SubstituteStringEntry",
    {
        "source": "aws_sdk_cloudwatch_logs.types.source.Source",
        "from": "aws_sdk_cloudwatch_logs.types.from_key.FromKey",
        "to": "aws_sdk_cloudwatch_logs.types.to_key.ToKey",
    },
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubstituteStringEntry) -> dict:
    out: dict = {}
    out["source"] = value["source"]
    out["from"] = value["from"]
    out["to"] = value["to"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SubstituteStringEntry:
    out: SubstituteStringEntry = {}  # type: ignore[typeddict-item]
    if "source" in data:
        out["source"] = data["source"]
    else:
        raise DeserializationError("SubstituteStringEntry.source required")
    if "from" in data:
        out["from"] = data["from"]
    else:
        raise DeserializationError("SubstituteStringEntry.from required")
    if "to" in data:
        out["to"] = data["to"]
    else:
        raise DeserializationError("SubstituteStringEntry.to required")
    return out
