"""Generated from Smithy shape ``com.amazonaws.omics#RunGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.run_group_list_item

RunGroupList: TypeAlias = list[
    "aws_sdk_omics.types.run_group_list_item.RunGroupListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: RunGroupList) -> list:
    import aws_sdk_omics.types.run_group_list_item

    out: list = []
    for item in value:
        out.append(aws_sdk_omics.types.run_group_list_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> RunGroupList:
    import aws_sdk_omics.types.run_group_list_item

    out: RunGroupList = []
    for item in data:
        out.append(aws_sdk_omics.types.run_group_list_item.deserialize_json(item))
    return out
