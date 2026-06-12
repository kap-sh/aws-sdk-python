"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#AddKeyEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.add_key_entry

AddKeyEntries: TypeAlias = list[
    "aws_sdk_cloudwatch_logs.types.add_key_entry.AddKeyEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddKeyEntries) -> list:
    import aws_sdk_cloudwatch_logs.types.add_key_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_logs.types.add_key_entry.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AddKeyEntries:
    import aws_sdk_cloudwatch_logs.types.add_key_entry

    out: AddKeyEntries = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_logs.types.add_key_entry.deserialize_aws_json_1_1(item)
        )
    return out
