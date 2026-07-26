"""Generated from Smithy shape ``com.amazonaws.repostspace#AccessorIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_repostspace.types.accessor_id

AccessorIdList: TypeAlias = list["capo_repostspace.types.accessor_id.AccessorId"]


# --- restJson1 ser/de ---
def serialize_json(value: AccessorIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> AccessorIdList:
    return list(data)
