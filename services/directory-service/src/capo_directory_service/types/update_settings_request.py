"""Generated from Smithy shape ``com.amazonaws.directoryservice#UpdateSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.settings


class UpdateSettingsRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the directory for which to update settings.</p>"""
    settings: "capo_directory_service.types.settings.Settings"
    """<p>The list of <a>Setting</a> objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSettingsRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    import capo_directory_service.types.settings

    out["Settings"] = capo_directory_service.types.settings.serialize_aws_json_1_1(
        value["settings"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSettingsRequest:
    out: UpdateSettingsRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError("UpdateSettingsRequest.directory_id required")
    if "Settings" in data:
        import capo_directory_service.types.settings

        out["settings"] = (
            capo_directory_service.types.settings.deserialize_aws_json_1_1(
                data["Settings"]
            )
        )
    else:
        raise DeserializationError("UpdateSettingsRequest.settings required")
    return out
