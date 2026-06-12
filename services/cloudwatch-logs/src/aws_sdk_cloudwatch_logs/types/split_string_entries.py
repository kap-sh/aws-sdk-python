"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#SplitStringEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.split_string_entry

SplitStringEntries: TypeAlias = list[
    "aws_sdk_cloudwatch_logs.types.split_string_entry.SplitStringEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SplitStringEntries) -> list:
    import aws_sdk_cloudwatch_logs.types.split_string_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_logs.types.split_string_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SplitStringEntries:
    import aws_sdk_cloudwatch_logs.types.split_string_entry

    out: SplitStringEntries = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_logs.types.split_string_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
