"""Generated from Smithy shape ``com.amazonaws.deadline#AllowedStorageProfileIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.storage_profile_id

AllowedStorageProfileIds: TypeAlias = list[
    "capo_deadline.types.storage_profile_id.StorageProfileId"
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedStorageProfileIds) -> list:
    return list(value)


def deserialize_json(data: list) -> AllowedStorageProfileIds:
    return list(data)
