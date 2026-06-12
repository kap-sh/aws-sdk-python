"""Generated from Smithy shape ``com.amazonaws.deadline#GetStorageProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.storage_profile_id


class GetStorageProfileRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID for the storage profile.</p>"""
    storage_profile_id: "aws_sdk_deadline.types.storage_profile_id.StorageProfileId"
    """<p>The storage profile ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStorageProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetStorageProfileRequest:
    out: GetStorageProfileRequest = {}  # type: ignore[typeddict-item]
    return out
