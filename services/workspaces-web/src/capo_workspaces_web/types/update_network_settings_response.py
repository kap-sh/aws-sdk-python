"""Generated from Smithy shape ``com.amazonaws.workspacesweb#UpdateNetworkSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces_web.types.network_settings


class UpdateNetworkSettingsResponse(TypedDict, closed=True):
    network_settings: "capo_workspaces_web.types.network_settings.NetworkSettings"
    """<p>The network settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNetworkSettingsResponse) -> dict:
    out: dict = {}
    import capo_workspaces_web.types.network_settings

    out["networkSettings"] = capo_workspaces_web.types.network_settings.serialize_json(
        value["network_settings"]
    )
    return out


def deserialize_json(data: dict) -> UpdateNetworkSettingsResponse:
    out: UpdateNetworkSettingsResponse = {}  # type: ignore[typeddict-item]
    if "networkSettings" in data:
        import capo_workspaces_web.types.network_settings

        out["network_settings"] = (
            capo_workspaces_web.types.network_settings.deserialize_json(
                data["networkSettings"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateNetworkSettingsResponse.network_settings required"
        )
    return out
