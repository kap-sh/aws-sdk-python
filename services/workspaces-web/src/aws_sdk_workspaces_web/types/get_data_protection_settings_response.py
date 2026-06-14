"""Generated from Smithy shape ``com.amazonaws.workspacesweb#GetDataProtectionSettingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.data_protection_settings


class GetDataProtectionSettingsResponse(TypedDict):
    data_protection_settings: NotRequired[
        "aws_sdk_workspaces_web.types.data_protection_settings.DataProtectionSettings"
    ]
    """<p>The data protection settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataProtectionSettingsResponse) -> dict:
    out: dict = {}
    if "data_protection_settings" in value:
        import aws_sdk_workspaces_web.types.data_protection_settings

        out["dataProtectionSettings"] = (
            aws_sdk_workspaces_web.types.data_protection_settings.serialize_json(
                value["data_protection_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetDataProtectionSettingsResponse:
    out: GetDataProtectionSettingsResponse = {}  # type: ignore[typeddict-item]
    if "dataProtectionSettings" in data:
        import aws_sdk_workspaces_web.types.data_protection_settings

        out["data_protection_settings"] = (
            aws_sdk_workspaces_web.types.data_protection_settings.deserialize_json(
                data["dataProtectionSettings"]
            )
        )
    return out
