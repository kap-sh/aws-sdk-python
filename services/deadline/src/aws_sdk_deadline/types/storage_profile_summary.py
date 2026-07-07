"""Generated from Smithy shape ``com.amazonaws.deadline#StorageProfileSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.resource_name
    import aws_sdk_deadline.types.storage_profile_id
    import aws_sdk_deadline.types.storage_profile_operating_system_family


class StorageProfileSummary(TypedDict, closed=True):
    storage_profile_id: "aws_sdk_deadline.types.storage_profile_id.StorageProfileId"
    """<p>The storage profile ID.</p>"""
    display_name: "aws_sdk_deadline.types.resource_name.ResourceName"
    """<p>The display name of the storage profile summary to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    os_family: "aws_sdk_deadline.types.storage_profile_operating_system_family.StorageProfileOperatingSystemFamily"
    """<p>The operating system (OS) family.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StorageProfileSummary) -> dict:
    out: dict = {}
    out["storageProfileId"] = value["storage_profile_id"]
    out["displayName"] = value["display_name"]
    import aws_sdk_deadline.types.storage_profile_operating_system_family

    out["osFamily"] = (
        aws_sdk_deadline.types.storage_profile_operating_system_family.serialize_json(
            value["os_family"]
        )
    )
    return out


def deserialize_json(data: dict) -> StorageProfileSummary:
    out: StorageProfileSummary = {}  # type: ignore[typeddict-item]
    if "storageProfileId" in data:
        out["storage_profile_id"] = data["storageProfileId"]
    else:
        raise DeserializationError("StorageProfileSummary.storage_profile_id required")
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("StorageProfileSummary.display_name required")
    if "osFamily" in data:
        import aws_sdk_deadline.types.storage_profile_operating_system_family

        out["os_family"] = (
            aws_sdk_deadline.types.storage_profile_operating_system_family.deserialize_json(
                data["osFamily"]
            )
        )
    else:
        raise DeserializationError("StorageProfileSummary.os_family required")
    return out
