"""Generated from Smithy shape ``com.amazonaws.wickr#GetNetworkSettingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.settings_list


class GetNetworkSettingsResponse(TypedDict):
    settings: "aws_sdk_wickr.types.settings_list.SettingsList"
    """<p>A list of network settings, where each setting includes a name, value, and type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNetworkSettingsResponse) -> dict:
    out: dict = {}
    import aws_sdk_wickr.types.settings_list

    out["settings"] = aws_sdk_wickr.types.settings_list.serialize_json(
        value["settings"]
    )
    return out


def deserialize_json(data: dict) -> GetNetworkSettingsResponse:
    out: GetNetworkSettingsResponse = {}  # type: ignore[typeddict-item]
    if "settings" in data:
        import aws_sdk_wickr.types.settings_list

        out["settings"] = aws_sdk_wickr.types.settings_list.deserialize_json(
            data["settings"]
        )
    else:
        raise DeserializationError("GetNetworkSettingsResponse.settings required")
    return out
