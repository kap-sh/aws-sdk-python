"""Generated from Smithy shape ``com.amazonaws.qapps#UpdateLibraryItemMetadataInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.instance_id
    import aws_sdk_qapps.types.uuid


class UpdateLibraryItemMetadataInput(TypedDict):
    instance_id: "aws_sdk_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    library_item_id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The unique identifier of the updated library item.</p>"""
    is_verified: NotRequired["bool"]
    """<p>The verification status of the library item</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLibraryItemMetadataInput) -> dict:
    out: dict = {}
    out["libraryItemId"] = value["library_item_id"]
    if "is_verified" in value:
        out["isVerified"] = value["is_verified"]
    return out


def deserialize_json(data: dict) -> UpdateLibraryItemMetadataInput:
    out: UpdateLibraryItemMetadataInput = {}  # type: ignore[typeddict-item]
    if "libraryItemId" in data:
        out["library_item_id"] = data["libraryItemId"]
    else:
        raise DeserializationError(
            "UpdateLibraryItemMetadataInput.library_item_id required"
        )
    if "isVerified" in data:
        out["is_verified"] = data["isVerified"]
    return out
