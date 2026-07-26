"""Generated from Smithy shape ``com.amazonaws.mgn#ApplicationIDs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.application_id

ApplicationIDs: TypeAlias = list["capo_mgn.types.application_id.ApplicationID"]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationIDs) -> list:
    return list(value)


def deserialize_json(data: list) -> ApplicationIDs:
    return list(data)
