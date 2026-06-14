"""Generated from Smithy shape ``com.amazonaws.workspacesweb#CreateIpAccessSettingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn


class CreateIpAccessSettingsResponse(TypedDict):
    ip_access_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the IP access settings resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIpAccessSettingsResponse) -> dict:
    out: dict = {}
    out["ipAccessSettingsArn"] = value["ip_access_settings_arn"]
    return out


def deserialize_json(data: dict) -> CreateIpAccessSettingsResponse:
    out: CreateIpAccessSettingsResponse = {}  # type: ignore[typeddict-item]
    if "ipAccessSettingsArn" in data:
        out["ip_access_settings_arn"] = data["ipAccessSettingsArn"]
    else:
        raise DeserializationError(
            "CreateIpAccessSettingsResponse.ip_access_settings_arn required"
        )
    return out
