"""Generated from Smithy shape ``com.amazonaws.eventbridge#TargetIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridge.types.target_id

TargetIdList: TypeAlias = list["capo_eventbridge.types.target_id.TargetId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TargetIdList:
    return [item for item in data if item is not None]
