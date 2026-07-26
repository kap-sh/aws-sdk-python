"""Generated from Smithy shape ``com.amazonaws.mgn#MergeConstructs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.merge_construct

MergeConstructs: TypeAlias = list["capo_mgn.types.merge_construct.MergeConstruct"]


# --- restJson1 ser/de ---
def serialize_json(value: MergeConstructs) -> list:
    import capo_mgn.types.merge_construct

    out: list = []
    for item in value:
        out.append(capo_mgn.types.merge_construct.serialize_json(item))
    return out


def deserialize_json(data: list) -> MergeConstructs:
    import capo_mgn.types.merge_construct

    out: MergeConstructs = []
    for item in data:
        out.append(capo_mgn.types.merge_construct.deserialize_json(item))
    return out
