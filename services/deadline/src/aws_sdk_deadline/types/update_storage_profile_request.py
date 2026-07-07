"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateStorageProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.client_token
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.file_system_locations_list
    import aws_sdk_deadline.types.resource_name
    import aws_sdk_deadline.types.storage_profile_id
    import aws_sdk_deadline.types.storage_profile_operating_system_family


class UpdateStorageProfileRequest(TypedDict, closed=True):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID to update.</p>"""
    storage_profile_id: "aws_sdk_deadline.types.storage_profile_id.StorageProfileId"
    """<p>The storage profile ID to update.</p>"""
    client_token: NotRequired["aws_sdk_deadline.types.client_token.ClientToken"]
    """<p>The unique token which the server uses to recognize retries of the same request.</p>"""
    display_name: NotRequired["aws_sdk_deadline.types.resource_name.ResourceName"]
    """<p>The display name of the storage profile to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    os_family: NotRequired[
        "aws_sdk_deadline.types.storage_profile_operating_system_family.StorageProfileOperatingSystemFamily"
    ]
    """<p>The OS system to update.</p>"""
    file_system_locations_to_add: NotRequired[
        "aws_sdk_deadline.types.file_system_locations_list.FileSystemLocationsList"
    ]
    """<p>The file system location names to add.</p>"""
    file_system_locations_to_remove: NotRequired[
        "aws_sdk_deadline.types.file_system_locations_list.FileSystemLocationsList"
    ]
    """<p>The file system location names to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateStorageProfileRequest) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "os_family" in value:
        import aws_sdk_deadline.types.storage_profile_operating_system_family

        out["osFamily"] = (
            aws_sdk_deadline.types.storage_profile_operating_system_family.serialize_json(
                value["os_family"]
            )
        )
    if "file_system_locations_to_add" in value:
        import aws_sdk_deadline.types.file_system_locations_list

        out["fileSystemLocationsToAdd"] = (
            aws_sdk_deadline.types.file_system_locations_list.serialize_json(
                value["file_system_locations_to_add"]
            )
        )
    if "file_system_locations_to_remove" in value:
        import aws_sdk_deadline.types.file_system_locations_list

        out["fileSystemLocationsToRemove"] = (
            aws_sdk_deadline.types.file_system_locations_list.serialize_json(
                value["file_system_locations_to_remove"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateStorageProfileRequest:
    out: UpdateStorageProfileRequest = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "osFamily" in data:
        import aws_sdk_deadline.types.storage_profile_operating_system_family

        out["os_family"] = (
            aws_sdk_deadline.types.storage_profile_operating_system_family.deserialize_json(
                data["osFamily"]
            )
        )
    if "fileSystemLocationsToAdd" in data:
        import aws_sdk_deadline.types.file_system_locations_list

        out["file_system_locations_to_add"] = (
            aws_sdk_deadline.types.file_system_locations_list.deserialize_json(
                data["fileSystemLocationsToAdd"]
            )
        )
    if "fileSystemLocationsToRemove" in data:
        import aws_sdk_deadline.types.file_system_locations_list

        out["file_system_locations_to_remove"] = (
            aws_sdk_deadline.types.file_system_locations_list.deserialize_json(
                data["fileSystemLocationsToRemove"]
            )
        )
    return out
