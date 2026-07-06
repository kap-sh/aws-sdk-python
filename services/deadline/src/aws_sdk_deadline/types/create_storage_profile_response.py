"""Generated from Smithy shape ``com.amazonaws.deadline#CreateStorageProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.storage_profile_id


class CreateStorageProfileResponse(TypedDict, closed=True):
    storage_profile_id: "aws_sdk_deadline.types.storage_profile_id.StorageProfileId"
    """<p>The storage profile ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateStorageProfileResponse) -> dict:
    out: dict = {}
    out["storageProfileId"] = value["storage_profile_id"]
    return out


def deserialize_json(data: dict) -> CreateStorageProfileResponse:
    out: CreateStorageProfileResponse = {}  # type: ignore[typeddict-item]
    if "storageProfileId" in data:
        out["storage_profile_id"] = data["storageProfileId"]
    else:
        raise DeserializationError(
            "CreateStorageProfileResponse.storage_profile_id required"
        )
    return out
