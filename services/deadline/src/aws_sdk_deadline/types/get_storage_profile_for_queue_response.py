"""Generated from Smithy shape ``com.amazonaws.deadline#GetStorageProfileForQueueResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.file_system_locations_list
    import aws_sdk_deadline.types.resource_name
    import aws_sdk_deadline.types.storage_profile_id
    import aws_sdk_deadline.types.storage_profile_operating_system_family


class GetStorageProfileForQueueResponse(TypedDict):
    storage_profile_id: "aws_sdk_deadline.types.storage_profile_id.StorageProfileId"
    """<p>The storage profile ID.</p>"""
    display_name: "aws_sdk_deadline.types.resource_name.ResourceName"
    """<p>The display name of the storage profile connected to a queue.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    os_family: "aws_sdk_deadline.types.storage_profile_operating_system_family.StorageProfileOperatingSystemFamily"
    """<p>The operating system of the storage profile in the queue.</p>"""
    file_system_locations: NotRequired[
        "aws_sdk_deadline.types.file_system_locations_list.FileSystemLocationsList"
    ]
    """<p>The location of the files for the storage profile within the queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStorageProfileForQueueResponse) -> dict:
    out: dict = {}
    out["storageProfileId"] = value["storage_profile_id"]
    out["displayName"] = value["display_name"]
    import aws_sdk_deadline.types.storage_profile_operating_system_family

    out["osFamily"] = (
        aws_sdk_deadline.types.storage_profile_operating_system_family.serialize_json(
            value["os_family"]
        )
    )
    if "file_system_locations" in value:
        import aws_sdk_deadline.types.file_system_locations_list

        out["fileSystemLocations"] = (
            aws_sdk_deadline.types.file_system_locations_list.serialize_json(
                value["file_system_locations"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetStorageProfileForQueueResponse:
    out: GetStorageProfileForQueueResponse = {}  # type: ignore[typeddict-item]
    if "storageProfileId" in data:
        out["storage_profile_id"] = data["storageProfileId"]
    else:
        raise DeserializationError(
            "GetStorageProfileForQueueResponse.storage_profile_id required"
        )
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError(
            "GetStorageProfileForQueueResponse.display_name required"
        )
    if "osFamily" in data:
        import aws_sdk_deadline.types.storage_profile_operating_system_family

        out["os_family"] = (
            aws_sdk_deadline.types.storage_profile_operating_system_family.deserialize_json(
                data["osFamily"]
            )
        )
    else:
        raise DeserializationError(
            "GetStorageProfileForQueueResponse.os_family required"
        )
    if "fileSystemLocations" in data:
        import aws_sdk_deadline.types.file_system_locations_list

        out["file_system_locations"] = (
            aws_sdk_deadline.types.file_system_locations_list.deserialize_json(
                data["fileSystemLocations"]
            )
        )
    return out
