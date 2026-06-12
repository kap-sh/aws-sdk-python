"""Generated from Smithy shape ``com.amazonaws.gamelift#PriorityTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.priority_type

PriorityTypeList: TypeAlias = list["aws_sdk_gamelift.types.priority_type.PriorityType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PriorityTypeList) -> list:
    import aws_sdk_gamelift.types.priority_type

    out: list = []
    for item in value:
        out.append(aws_sdk_gamelift.types.priority_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PriorityTypeList:
    import aws_sdk_gamelift.types.priority_type

    out: PriorityTypeList = []
    for item in data:
        out.append(aws_sdk_gamelift.types.priority_type.deserialize_aws_json_1_1(item))
    return out
