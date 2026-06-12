"""Generated from Smithy shape ``com.amazonaws.connect#TagOrConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.tag_and_condition_list

TagOrConditionList: TypeAlias = list[
    "aws_sdk_connect.types.tag_and_condition_list.TagAndConditionList"
]


# --- restJson1 ser/de ---
def serialize_json(value: TagOrConditionList) -> list:
    import aws_sdk_connect.types.tag_and_condition_list

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.tag_and_condition_list.serialize_json(item))
    return out


def deserialize_json(data: list) -> TagOrConditionList:
    import aws_sdk_connect.types.tag_and_condition_list

    out: TagOrConditionList = []
    for item in data:
        out.append(aws_sdk_connect.types.tag_and_condition_list.deserialize_json(item))
    return out
