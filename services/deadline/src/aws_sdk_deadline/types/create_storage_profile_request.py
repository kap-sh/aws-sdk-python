"""Generated from Smithy shape ``com.amazonaws.deadline#CreateStorageProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.client_token
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.file_system_locations_list
    import aws_sdk_deadline.types.resource_name
    import aws_sdk_deadline.types.storage_profile_operating_system_family


class CreateStorageProfileRequest(TypedDict, closed=True):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the farm to connect to the storage profile.</p>"""
    client_token: NotRequired["aws_sdk_deadline.types.client_token.ClientToken"]
    """<p>The unique token which the server uses to recognize retries of the same request.</p>"""
    display_name: "aws_sdk_deadline.types.resource_name.ResourceName"
    """<p>The display name of the storage profile.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    os_family: "aws_sdk_deadline.types.storage_profile_operating_system_family.StorageProfileOperatingSystemFamily"
    """<p>The type of operating system (OS) for the storage profile.</p>"""
    file_system_locations: NotRequired[
        "aws_sdk_deadline.types.file_system_locations_list.FileSystemLocationsList"
    ]
    """<p>File system paths to include in the storage profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateStorageProfileRequest) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> CreateStorageProfileRequest:
    out: CreateStorageProfileRequest = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("CreateStorageProfileRequest.display_name required")
    if "osFamily" in data:
        import aws_sdk_deadline.types.storage_profile_operating_system_family

        out["os_family"] = (
            aws_sdk_deadline.types.storage_profile_operating_system_family.deserialize_json(
                data["osFamily"]
            )
        )
    else:
        raise DeserializationError("CreateStorageProfileRequest.os_family required")
    if "fileSystemLocations" in data:
        import aws_sdk_deadline.types.file_system_locations_list

        out["file_system_locations"] = (
            aws_sdk_deadline.types.file_system_locations_list.deserialize_json(
                data["fileSystemLocations"]
            )
        )
    return out
