"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#GroupResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotdeviceadvisor.types.group_result

GroupResultList: TypeAlias = list[
    "aws_sdk_iotdeviceadvisor.types.group_result.GroupResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupResultList) -> list:
    import aws_sdk_iotdeviceadvisor.types.group_result

    out: list = []
    for item in value:
        out.append(aws_sdk_iotdeviceadvisor.types.group_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroupResultList:
    import aws_sdk_iotdeviceadvisor.types.group_result

    out: GroupResultList = []
    for item in data:
        out.append(aws_sdk_iotdeviceadvisor.types.group_result.deserialize_json(item))
    return out
