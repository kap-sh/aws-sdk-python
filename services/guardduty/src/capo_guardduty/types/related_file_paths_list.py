"""Generated from Smithy shape ``com.amazonaws.guardduty#RelatedFilePathsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.string

RelatedFilePathsList: TypeAlias = list["capo_guardduty.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: RelatedFilePathsList) -> list:
    return list(value)


def deserialize_json(data: list) -> RelatedFilePathsList:
    return list(data)
