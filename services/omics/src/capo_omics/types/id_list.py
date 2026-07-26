"""Generated from Smithy shape ``com.amazonaws.omics#IdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.resource_identifier

IdList: TypeAlias = list["capo_omics.types.resource_identifier.ResourceIdentifier"]


# --- restJson1 ser/de ---
def serialize_json(value: IdList) -> list:
    return list(value)


def deserialize_json(data: list) -> IdList:
    return list(data)
