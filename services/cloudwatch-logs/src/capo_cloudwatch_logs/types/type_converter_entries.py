"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#TypeConverterEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.type_converter_entry

TypeConverterEntries: TypeAlias = list[
    "capo_cloudwatch_logs.types.type_converter_entry.TypeConverterEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TypeConverterEntries) -> list:
    import capo_cloudwatch_logs.types.type_converter_entry

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_logs.types.type_converter_entry.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TypeConverterEntries:
    import capo_cloudwatch_logs.types.type_converter_entry

    out: TypeConverterEntries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch_logs.types.type_converter_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
