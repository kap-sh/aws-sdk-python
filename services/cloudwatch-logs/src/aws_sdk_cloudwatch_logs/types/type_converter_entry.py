"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#TypeConverterEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.key
    import aws_sdk_cloudwatch_logs.types.type


class TypeConverterEntry(TypedDict, closed=True):
    key: "aws_sdk_cloudwatch_logs.types.key.Key"
    """<p>The key with the value that is to be converted to a different type.</p>"""
    type: "aws_sdk_cloudwatch_logs.types.type.Type"
    """<p>The type to convert the field value to. Valid values are <code>integer</code>, <code>double</code>, <code>string</code> and <code>boolean</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TypeConverterEntry) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import aws_sdk_cloudwatch_logs.types.type

    out["type"] = aws_sdk_cloudwatch_logs.types.type.serialize_aws_json_1_1(
        value["type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TypeConverterEntry:
    out: TypeConverterEntry = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("TypeConverterEntry.key required")
    if "type" in data:
        import aws_sdk_cloudwatch_logs.types.type

        out["type"] = aws_sdk_cloudwatch_logs.types.type.deserialize_aws_json_1_1(
            data["type"]
        )
    else:
        raise DeserializationError("TypeConverterEntry.type required")
    return out
