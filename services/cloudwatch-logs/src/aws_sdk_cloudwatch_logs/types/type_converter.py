"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#TypeConverter``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.type_converter_entries


class TypeConverter(TypedDict):
    entries: "aws_sdk_cloudwatch_logs.types.type_converter_entries.TypeConverterEntries"
    """<p>An array of <code>TypeConverterEntry</code> objects, where each object contains the information about one field to change the type of. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TypeConverter) -> dict:
    out: dict = {}
    import aws_sdk_cloudwatch_logs.types.type_converter_entries

    out["entries"] = (
        aws_sdk_cloudwatch_logs.types.type_converter_entries.serialize_aws_json_1_1(
            value["entries"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TypeConverter:
    out: TypeConverter = {}  # type: ignore[typeddict-item]
    if "entries" in data:
        import aws_sdk_cloudwatch_logs.types.type_converter_entries

        out["entries"] = (
            aws_sdk_cloudwatch_logs.types.type_converter_entries.deserialize_aws_json_1_1(
                data["entries"]
            )
        )
    else:
        raise DeserializationError("TypeConverter.entries required")
    return out
