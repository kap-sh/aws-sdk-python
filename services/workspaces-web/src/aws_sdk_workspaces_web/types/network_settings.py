"""Generated from Smithy shape ``com.amazonaws.workspacesweb#NetworkSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn
    import aws_sdk_workspaces_web.types.arn_list
    import aws_sdk_workspaces_web.types.security_group_id_list
    import aws_sdk_workspaces_web.types.subnet_id_list
    import aws_sdk_workspaces_web.types.vpc_id


class NetworkSettings(TypedDict):
    network_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the network settings.</p>"""
    associated_portal_arns: NotRequired["aws_sdk_workspaces_web.types.arn_list.ArnList"]
    """<p>A list of web portal ARNs that this network settings is associated with.</p>"""
    vpc_id: NotRequired["aws_sdk_workspaces_web.types.vpc_id.VpcId"]
    """<p>The VPC that streaming instances will connect to.</p>"""
    subnet_ids: NotRequired["aws_sdk_workspaces_web.types.subnet_id_list.SubnetIdList"]
    """<p>The subnets in which network interfaces are created to connect streaming instances to your VPC. At least two of these subnets must be in different availability zones.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_workspaces_web.types.security_group_id_list.SecurityGroupIdList"
    ]
    """<p>One or more security groups used to control access from streaming instances to your VPC. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkSettings) -> dict:
    out: dict = {}
    out["networkSettingsArn"] = value["network_settings_arn"]
    if "associated_portal_arns" in value:
        import aws_sdk_workspaces_web.types.arn_list

        out["associatedPortalArns"] = (
            aws_sdk_workspaces_web.types.arn_list.serialize_json(
                value["associated_portal_arns"]
            )
        )
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "subnet_ids" in value:
        import aws_sdk_workspaces_web.types.subnet_id_list

        out["subnetIds"] = aws_sdk_workspaces_web.types.subnet_id_list.serialize_json(
            value["subnet_ids"]
        )
    if "security_group_ids" in value:
        import aws_sdk_workspaces_web.types.security_group_id_list

        out["securityGroupIds"] = (
            aws_sdk_workspaces_web.types.security_group_id_list.serialize_json(
                value["security_group_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> NetworkSettings:
    out: NetworkSettings = {}  # type: ignore[typeddict-item]
    if "networkSettingsArn" in data:
        out["network_settings_arn"] = data["networkSettingsArn"]
    else:
        raise DeserializationError("NetworkSettings.network_settings_arn required")
    if "associatedPortalArns" in data:
        import aws_sdk_workspaces_web.types.arn_list

        out["associated_portal_arns"] = (
            aws_sdk_workspaces_web.types.arn_list.deserialize_json(
                data["associatedPortalArns"]
            )
        )
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    if "subnetIds" in data:
        import aws_sdk_workspaces_web.types.subnet_id_list

        out["subnet_ids"] = (
            aws_sdk_workspaces_web.types.subnet_id_list.deserialize_json(
                data["subnetIds"]
            )
        )
    if "securityGroupIds" in data:
        import aws_sdk_workspaces_web.types.security_group_id_list

        out["security_group_ids"] = (
            aws_sdk_workspaces_web.types.security_group_id_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    return out
