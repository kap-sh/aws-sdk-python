"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#RenameKeyEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.rename_key_entry

RenameKeyEntries: TypeAlias = list[
    "capo_cloudwatch_logs.types.rename_key_entry.RenameKeyEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RenameKeyEntries) -> list:
    import capo_cloudwatch_logs.types.rename_key_entry

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_logs.types.rename_key_entry.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RenameKeyEntries:
    import capo_cloudwatch_logs.types.rename_key_entry

    out: RenameKeyEntries = []
    for item in data:
        out.append(
            capo_cloudwatch_logs.types.rename_key_entry.deserialize_aws_json_1_1(item)
        )
    return out
