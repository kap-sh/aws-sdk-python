"""Generated from Smithy shape ``com.amazonaws.eventbridge#PutTargetsResultEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.put_targets_result_entry

PutTargetsResultEntryList: TypeAlias = list[
    "aws_sdk_eventbridge.types.put_targets_result_entry.PutTargetsResultEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutTargetsResultEntryList) -> list:
    import aws_sdk_eventbridge.types.put_targets_result_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_eventbridge.types.put_targets_result_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PutTargetsResultEntryList:
    import aws_sdk_eventbridge.types.put_targets_result_entry

    out: PutTargetsResultEntryList = []
    for item in data:
        out.append(
            aws_sdk_eventbridge.types.put_targets_result_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
