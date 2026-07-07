"""Generated from Smithy shape ``com.amazonaws.workspacesweb#NetworkSettingsSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn
    import aws_sdk_workspaces_web.types.vpc_id


class NetworkSettingsSummary(TypedDict, closed=True):
    network_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the network settings.</p>"""
    vpc_id: NotRequired["aws_sdk_workspaces_web.types.vpc_id.VpcId"]
    """<p>The VPC ID of the network settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkSettingsSummary) -> dict:
    out: dict = {}
    out["networkSettingsArn"] = value["network_settings_arn"]
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    return out


def deserialize_json(data: dict) -> NetworkSettingsSummary:
    out: NetworkSettingsSummary = {}  # type: ignore[typeddict-item]
    if "networkSettingsArn" in data:
        out["network_settings_arn"] = data["networkSettingsArn"]
    else:
        raise DeserializationError(
            "NetworkSettingsSummary.network_settings_arn required"
        )
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    return out
