"""Generated from Smithy shape ``com.amazonaws.wickr#UpdateNetworkSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.settings_list


class UpdateNetworkSettingsResponse(TypedDict, closed=True):
    settings: "aws_sdk_wickr.types.settings_list.SettingsList"
    """<p>A list of the updated network settings, showing the new values for each modified setting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNetworkSettingsResponse) -> dict:
    out: dict = {}
    import aws_sdk_wickr.types.settings_list

    out["settings"] = aws_sdk_wickr.types.settings_list.serialize_json(
        value["settings"]
    )
    return out


def deserialize_json(data: dict) -> UpdateNetworkSettingsResponse:
    out: UpdateNetworkSettingsResponse = {}  # type: ignore[typeddict-item]
    if "settings" in data:
        import aws_sdk_wickr.types.settings_list

        out["settings"] = aws_sdk_wickr.types.settings_list.deserialize_json(
            data["settings"]
        )
    else:
        raise DeserializationError("UpdateNetworkSettingsResponse.settings required")
    return out
