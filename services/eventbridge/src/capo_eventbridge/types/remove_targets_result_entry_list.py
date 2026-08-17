"""Generated from Smithy shape ``com.amazonaws.eventbridge#RemoveTargetsResultEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridge.types.remove_targets_result_entry

RemoveTargetsResultEntryList: TypeAlias = list[
    "capo_eventbridge.types.remove_targets_result_entry.RemoveTargetsResultEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveTargetsResultEntryList) -> list:
    import capo_eventbridge.types.remove_targets_result_entry

    out: list = []
    for item in value:
        out.append(
            capo_eventbridge.types.remove_targets_result_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RemoveTargetsResultEntryList:
    import capo_eventbridge.types.remove_targets_result_entry

    out: RemoveTargetsResultEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_eventbridge.types.remove_targets_result_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
