"""Generated from Smithy shape ``com.amazonaws.gamelift#PriorityTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.priority_type

PriorityTypeList: TypeAlias = list["capo_gamelift.types.priority_type.PriorityType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PriorityTypeList) -> list:
    import capo_gamelift.types.priority_type

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.priority_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PriorityTypeList:
    import capo_gamelift.types.priority_type

    out: PriorityTypeList = []
    for item in data:
        out.append(capo_gamelift.types.priority_type.deserialize_aws_json_1_1(item))
    return out
