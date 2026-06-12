"""Generated from Smithy shape ``com.amazonaws.deadline#DeleteStorageProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.storage_profile_id


class DeleteStorageProfileRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the farm from which to remove the storage profile.</p>"""
    storage_profile_id: "aws_sdk_deadline.types.storage_profile_id.StorageProfileId"
    """<p>The storage profile ID of the storage profile to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteStorageProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteStorageProfileRequest:
    out: DeleteStorageProfileRequest = {}  # type: ignore[typeddict-item]
    return out
