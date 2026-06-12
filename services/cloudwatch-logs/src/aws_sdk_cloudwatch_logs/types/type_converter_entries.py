"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#TypeConverterEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.type_converter_entry

TypeConverterEntries: TypeAlias = list[
    "aws_sdk_cloudwatch_logs.types.type_converter_entry.TypeConverterEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TypeConverterEntries) -> list:
    import aws_sdk_cloudwatch_logs.types.type_converter_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_logs.types.type_converter_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TypeConverterEntries:
    import aws_sdk_cloudwatch_logs.types.type_converter_entry

    out: TypeConverterEntries = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_logs.types.type_converter_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
