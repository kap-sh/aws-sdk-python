"""Generated from Smithy shape ``com.amazonaws.workspacesweb#UpdateIpAccessSettingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.ip_access_settings


class UpdateIpAccessSettingsResponse(TypedDict):
    ip_access_settings: (
        "aws_sdk_workspaces_web.types.ip_access_settings.IpAccessSettings"
    )
    """<p>The IP access settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIpAccessSettingsResponse) -> dict:
    out: dict = {}
    import aws_sdk_workspaces_web.types.ip_access_settings

    out["ipAccessSettings"] = (
        aws_sdk_workspaces_web.types.ip_access_settings.serialize_json(
            value["ip_access_settings"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateIpAccessSettingsResponse:
    out: UpdateIpAccessSettingsResponse = {}  # type: ignore[typeddict-item]
    if "ipAccessSettings" in data:
        import aws_sdk_workspaces_web.types.ip_access_settings

        out["ip_access_settings"] = (
            aws_sdk_workspaces_web.types.ip_access_settings.deserialize_json(
                data["ipAccessSettings"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateIpAccessSettingsResponse.ip_access_settings required"
        )
    return out
