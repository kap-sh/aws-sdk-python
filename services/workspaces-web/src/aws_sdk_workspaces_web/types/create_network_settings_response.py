"""Generated from Smithy shape ``com.amazonaws.workspacesweb#CreateNetworkSettingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn


class CreateNetworkSettingsResponse(TypedDict):
    network_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the network settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNetworkSettingsResponse) -> dict:
    out: dict = {}
    out["networkSettingsArn"] = value["network_settings_arn"]
    return out


def deserialize_json(data: dict) -> CreateNetworkSettingsResponse:
    out: CreateNetworkSettingsResponse = {}  # type: ignore[typeddict-item]
    if "networkSettingsArn" in data:
        out["network_settings_arn"] = data["networkSettingsArn"]
    else:
        raise DeserializationError(
            "CreateNetworkSettingsResponse.network_settings_arn required"
        )
    return out
