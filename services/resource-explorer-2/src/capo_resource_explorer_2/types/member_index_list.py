"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#MemberIndexList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.member_index

MemberIndexList: TypeAlias = list[
    "capo_resource_explorer_2.types.member_index.MemberIndex"
]


# --- restJson1 ser/de ---
def serialize_json(value: MemberIndexList) -> list:
    import capo_resource_explorer_2.types.member_index

    out: list = []
    for item in value:
        out.append(capo_resource_explorer_2.types.member_index.serialize_json(item))
    return out


def deserialize_json(data: list) -> MemberIndexList:
    import capo_resource_explorer_2.types.member_index

    out: MemberIndexList = []
    for item in data:
        out.append(capo_resource_explorer_2.types.member_index.deserialize_json(item))
    return out
