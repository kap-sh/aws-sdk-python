"""Generated from Smithy shape ``com.amazonaws.workspacesweb#GetIpAccessSettingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.ip_access_settings


class GetIpAccessSettingsResponse(TypedDict):
    ip_access_settings: NotRequired[
        "aws_sdk_workspaces_web.types.ip_access_settings.IpAccessSettings"
    ]
    """<p>The IP access settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIpAccessSettingsResponse) -> dict:
    out: dict = {}
    if "ip_access_settings" in value:
        import aws_sdk_workspaces_web.types.ip_access_settings

        out["ipAccessSettings"] = (
            aws_sdk_workspaces_web.types.ip_access_settings.serialize_json(
                value["ip_access_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetIpAccessSettingsResponse:
    out: GetIpAccessSettingsResponse = {}  # type: ignore[typeddict-item]
    if "ipAccessSettings" in data:
        import aws_sdk_workspaces_web.types.ip_access_settings

        out["ip_access_settings"] = (
            aws_sdk_workspaces_web.types.ip_access_settings.deserialize_json(
                data["ipAccessSettings"]
            )
        )
    return out
