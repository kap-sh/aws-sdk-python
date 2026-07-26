"""Generated from Smithy shape ``com.amazonaws.wickr#UpdateNetworkSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wickr.types.network_id
    import capo_wickr.types.network_settings


class UpdateNetworkSettingsRequest(TypedDict, closed=True):
    network_id: "capo_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network whose settings will be updated.</p>"""
    settings: "capo_wickr.types.network_settings.NetworkSettings"
    """<p>A map of setting names to their new values. Each setting should be provided with its appropriate type (boolean, string, number, etc.).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNetworkSettingsRequest) -> dict:
    out: dict = {}
    import capo_wickr.types.network_settings

    out["settings"] = capo_wickr.types.network_settings.serialize_json(
        value["settings"]
    )
    return out


def deserialize_json(data: dict) -> UpdateNetworkSettingsRequest:
    out: UpdateNetworkSettingsRequest = {}  # type: ignore[typeddict-item]
    if "settings" in data:
        import capo_wickr.types.network_settings

        out["settings"] = capo_wickr.types.network_settings.deserialize_json(
            data["settings"]
        )
    else:
        raise DeserializationError("UpdateNetworkSettingsRequest.settings required")
    return out
