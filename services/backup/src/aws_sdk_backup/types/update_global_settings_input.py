"""Generated from Smithy shape ``com.amazonaws.backup#UpdateGlobalSettingsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.global_settings


class UpdateGlobalSettingsInput(TypedDict):
    global_settings: NotRequired["aws_sdk_backup.types.global_settings.GlobalSettings"]
    """<p>Inputs can include:</p> <p>A value for <code>isCrossAccountBackupEnabled</code>. Values can be true or false. Example: <code>update-global-settings --global-settings isCrossAccountBackupEnabled=false</code>.</p> <p>A value for Multi-party approval, styled as <code>isMpaEnabled</code>. Values can be true or false. Example: <code>update-global-settings --global-settings isMpaEnabled=false</code>.</p> <p>A value for Backup Service-Linked Role creation, styled as <code>isDelegatedAdministratorEnabled</code>. Values can be true or false. Example: <code>update-global-settings --global-settings isDelegatedAdministratorEnabled=false</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGlobalSettingsInput) -> dict:
    out: dict = {}
    if "global_settings" in value:
        import aws_sdk_backup.types.global_settings

        out["GlobalSettings"] = aws_sdk_backup.types.global_settings.serialize_json(
            value["global_settings"]
        )
    return out


def deserialize_json(data: dict) -> UpdateGlobalSettingsInput:
    out: UpdateGlobalSettingsInput = {}  # type: ignore[typeddict-item]
    if "GlobalSettings" in data:
        import aws_sdk_backup.types.global_settings

        out["global_settings"] = aws_sdk_backup.types.global_settings.deserialize_json(
            data["GlobalSettings"]
        )
    return out
