"""Generated from Smithy shape ``com.amazonaws.health#DateTimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_health.types.timestamp

DateTimeRange = TypedDict(
    "DateTimeRange",
    {
        "from": NotRequired["aws_sdk_health.types.timestamp.timestamp"],
        "to": NotRequired["aws_sdk_health.types.timestamp.timestamp"],
    },
    closed=True,
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DateTimeRange) -> dict:
    out: dict = {}
    if "from" in value:
        import aws_sdk_health.types.timestamp

        out["from"] = aws_sdk_health.types.timestamp.serialize_aws_json_1_1(
            value["from"]
        )
    if "to" in value:
        import aws_sdk_health.types.timestamp

        out["to"] = aws_sdk_health.types.timestamp.serialize_aws_json_1_1(value["to"])
    return out


def deserialize_aws_json_1_1(data: dict) -> DateTimeRange:
    out: DateTimeRange = {}  # type: ignore[typeddict-item]
    if "from" in data:
        import aws_sdk_health.types.timestamp

        out["from"] = aws_sdk_health.types.timestamp.deserialize_aws_json_1_1(
            data["from"]
        )
    if "to" in data:
        import aws_sdk_health.types.timestamp

        out["to"] = aws_sdk_health.types.timestamp.deserialize_aws_json_1_1(data["to"])
    return out
