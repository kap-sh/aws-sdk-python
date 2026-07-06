"""Generated from Smithy shape ``com.amazonaws.workspacesweb#GetNetworkSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.network_settings


class GetNetworkSettingsResponse(TypedDict, closed=True):
    network_settings: NotRequired[
        "aws_sdk_workspaces_web.types.network_settings.NetworkSettings"
    ]
    """<p>The network settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNetworkSettingsResponse) -> dict:
    out: dict = {}
    if "network_settings" in value:
        import aws_sdk_workspaces_web.types.network_settings

        out["networkSettings"] = (
            aws_sdk_workspaces_web.types.network_settings.serialize_json(
                value["network_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetNetworkSettingsResponse:
    out: GetNetworkSettingsResponse = {}  # type: ignore[typeddict-item]
    if "networkSettings" in data:
        import aws_sdk_workspaces_web.types.network_settings

        out["network_settings"] = (
            aws_sdk_workspaces_web.types.network_settings.deserialize_json(
                data["networkSettings"]
            )
        )
    return out
