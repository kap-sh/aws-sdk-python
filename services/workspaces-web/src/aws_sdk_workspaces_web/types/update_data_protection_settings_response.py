"""Generated from Smithy shape ``com.amazonaws.workspacesweb#UpdateDataProtectionSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.data_protection_settings


class UpdateDataProtectionSettingsResponse(TypedDict, closed=True):
    data_protection_settings: (
        "aws_sdk_workspaces_web.types.data_protection_settings.DataProtectionSettings"
    )
    """<p>The data protection settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataProtectionSettingsResponse) -> dict:
    out: dict = {}
    import aws_sdk_workspaces_web.types.data_protection_settings

    out["dataProtectionSettings"] = (
        aws_sdk_workspaces_web.types.data_protection_settings.serialize_json(
            value["data_protection_settings"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateDataProtectionSettingsResponse:
    out: UpdateDataProtectionSettingsResponse = {}  # type: ignore[typeddict-item]
    if "dataProtectionSettings" in data:
        import aws_sdk_workspaces_web.types.data_protection_settings

        out["data_protection_settings"] = (
            aws_sdk_workspaces_web.types.data_protection_settings.deserialize_json(
                data["dataProtectionSettings"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateDataProtectionSettingsResponse.data_protection_settings required"
        )
    return out
