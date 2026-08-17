"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#MoveKeyEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.move_key_entry

MoveKeyEntries: TypeAlias = list[
    "capo_cloudwatch_logs.types.move_key_entry.MoveKeyEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MoveKeyEntries) -> list:
    import capo_cloudwatch_logs.types.move_key_entry

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_logs.types.move_key_entry.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MoveKeyEntries:
    import capo_cloudwatch_logs.types.move_key_entry

    out: MoveKeyEntries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch_logs.types.move_key_entry.deserialize_aws_json_1_1(item)
        )
    return out
