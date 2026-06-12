"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#CopyValueEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.copy_value_entry

CopyValueEntries: TypeAlias = list[
    "aws_sdk_cloudwatch_logs.types.copy_value_entry.CopyValueEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CopyValueEntries) -> list:
    import aws_sdk_cloudwatch_logs.types.copy_value_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_logs.types.copy_value_entry.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CopyValueEntries:
    import aws_sdk_cloudwatch_logs.types.copy_value_entry

    out: CopyValueEntries = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_logs.types.copy_value_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
