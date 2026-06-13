"""Generated from Smithy shape ``com.amazonaws.quicksight#UserIndexCapacityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.user_index_capacity

UserIndexCapacityList: TypeAlias = list[
    "aws_sdk_quicksight.types.user_index_capacity.UserIndexCapacity"
]


# --- restJson1 ser/de ---
def serialize_json(value: UserIndexCapacityList) -> list:
    import aws_sdk_quicksight.types.user_index_capacity

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.user_index_capacity.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserIndexCapacityList:
    import aws_sdk_quicksight.types.user_index_capacity

    out: UserIndexCapacityList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.user_index_capacity.deserialize_json(item))
    return out
