"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#RemoveTargetsResultEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.remove_targets_result_entry

RemoveTargetsResultEntryList: TypeAlias = list[
    "aws_sdk_cloudwatch_events.types.remove_targets_result_entry.RemoveTargetsResultEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveTargetsResultEntryList) -> list:
    import aws_sdk_cloudwatch_events.types.remove_targets_result_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_events.types.remove_targets_result_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RemoveTargetsResultEntryList:
    import aws_sdk_cloudwatch_events.types.remove_targets_result_entry

    out: RemoveTargetsResultEntryList = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_events.types.remove_targets_result_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
