"""Generated from Smithy shape ``com.amazonaws.quicksight#DecalSettingsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.decal_settings_list


class DecalSettingsConfiguration(TypedDict, closed=True):
    custom_decal_settings: NotRequired[
        "aws_sdk_quicksight.types.decal_settings_list.DecalSettingsList"
    ]
    """<p>A list of up to 50 decal settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DecalSettingsConfiguration) -> dict:
    out: dict = {}
    if "custom_decal_settings" in value:
        import aws_sdk_quicksight.types.decal_settings_list

        out["CustomDecalSettings"] = (
            aws_sdk_quicksight.types.decal_settings_list.serialize_json(
                value["custom_decal_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> DecalSettingsConfiguration:
    out: DecalSettingsConfiguration = {}  # type: ignore[typeddict-item]
    if "CustomDecalSettings" in data:
        import aws_sdk_quicksight.types.decal_settings_list

        out["custom_decal_settings"] = (
            aws_sdk_quicksight.types.decal_settings_list.deserialize_json(
                data["CustomDecalSettings"]
            )
        )
    return out
