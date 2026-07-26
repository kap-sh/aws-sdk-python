"""Generated from Smithy shape ``com.amazonaws.eks#labelsKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.string

labelsKeyList: TypeAlias = list["capo_eks.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: labelsKeyList) -> list:
    return list(value)


def deserialize_json(data: list) -> labelsKeyList:
    return list(data)
