"""Generated from Smithy shape ``com.amazonaws.omics#ReadSetIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.read_set_id

ReadSetIdList: TypeAlias = list["capo_omics.types.read_set_id.ReadSetId"]


# --- restJson1 ser/de ---
def serialize_json(value: ReadSetIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> ReadSetIdList:
    return list(data)
