"""Generated from Smithy shape ``com.amazonaws.omics#ReadSetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.read_set_list_item

ReadSetList: TypeAlias = list["aws_sdk_omics.types.read_set_list_item.ReadSetListItem"]


# --- restJson1 ser/de ---
def serialize_json(value: ReadSetList) -> list:
    import aws_sdk_omics.types.read_set_list_item

    out: list = []
    for item in value:
        out.append(aws_sdk_omics.types.read_set_list_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ReadSetList:
    import aws_sdk_omics.types.read_set_list_item

    out: ReadSetList = []
    for item in data:
        out.append(aws_sdk_omics.types.read_set_list_item.deserialize_json(item))
    return out
