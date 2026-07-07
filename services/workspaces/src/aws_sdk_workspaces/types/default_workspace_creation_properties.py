"""Generated from Smithy shape ``com.amazonaws.workspaces#DefaultWorkspaceCreationProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.arn
    import aws_sdk_workspaces.types.boolean_object
    import aws_sdk_workspaces.types.default_ou
    import aws_sdk_workspaces.types.security_group_id


class DefaultWorkspaceCreationProperties(TypedDict, closed=True):
    enable_internet_access: NotRequired[
        "aws_sdk_workspaces.types.boolean_object.BooleanObject"
    ]
    r"""<p>Specifies whether to automatically assign an Elastic public IP address to WorkSpaces in this directory by default. If enabled, the Elastic public IP address allows outbound internet access from your WorkSpaces when you’re using an internet gateway in the Amazon VPC in which your WorkSpaces are located. If you're using a Network Address Translation (NAT) gateway for outbound internet access from your VPC, or if your WorkSpaces are in public subnets and you manually assign them Elastic IP addresses, you should disable this setting. This setting applies to new WorkSpaces that you launch or to existing WorkSpaces that you rebuild. For more information, see <a href=\"https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-vpc.html\"> Configure a VPC for Amazon WorkSpaces</a>.</p>"""
    default_ou: NotRequired["aws_sdk_workspaces.types.default_ou.DefaultOu"]
    """<p>The organizational unit (OU) in the directory for the WorkSpace machine accounts.</p>"""
    custom_security_group_id: NotRequired[
        "aws_sdk_workspaces.types.security_group_id.SecurityGroupId"
    ]
    r"""<p>The identifier of the default security group to apply to WorkSpaces when they are created. For more information, see <a href=\"https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-security-groups.html\"> Security Groups for Your WorkSpaces</a>.</p>"""
    user_enabled_as_local_administrator: NotRequired[
        "aws_sdk_workspaces.types.boolean_object.BooleanObject"
    ]
    """<p>Specifies whether WorkSpace users are local administrators on their WorkSpaces.</p>"""
    enable_maintenance_mode: NotRequired[
        "aws_sdk_workspaces.types.boolean_object.BooleanObject"
    ]
    r"""<p>Specifies whether maintenance mode is enabled for WorkSpaces. For more information, see <a href=\"https://docs.aws.amazon.com/workspaces/latest/adminguide/workspace-maintenance.html\">WorkSpace Maintenance</a>.</p>"""
    instance_iam_role_arn: NotRequired["aws_sdk_workspaces.types.arn.ARN"]
    """<p>Indicates the IAM role ARN of the instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DefaultWorkspaceCreationProperties) -> dict:
    out: dict = {}
    if "enable_internet_access" in value:
        out["EnableInternetAccess"] = value["enable_internet_access"]
    if "default_ou" in value:
        out["DefaultOu"] = value["default_ou"]
    if "custom_security_group_id" in value:
        out["CustomSecurityGroupId"] = value["custom_security_group_id"]
    if "user_enabled_as_local_administrator" in value:
        out["UserEnabledAsLocalAdministrator"] = value[
            "user_enabled_as_local_administrator"
        ]
    if "enable_maintenance_mode" in value:
        out["EnableMaintenanceMode"] = value["enable_maintenance_mode"]
    if "instance_iam_role_arn" in value:
        out["InstanceIamRoleArn"] = value["instance_iam_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DefaultWorkspaceCreationProperties:
    out: DefaultWorkspaceCreationProperties = {}  # type: ignore[typeddict-item]
    if "EnableInternetAccess" in data:
        out["enable_internet_access"] = data["EnableInternetAccess"]
    if "DefaultOu" in data:
        out["default_ou"] = data["DefaultOu"]
    if "CustomSecurityGroupId" in data:
        out["custom_security_group_id"] = data["CustomSecurityGroupId"]
    if "UserEnabledAsLocalAdministrator" in data:
        out["user_enabled_as_local_administrator"] = data[
            "UserEnabledAsLocalAdministrator"
        ]
    if "EnableMaintenanceMode" in data:
        out["enable_maintenance_mode"] = data["EnableMaintenanceMode"]
    if "InstanceIamRoleArn" in data:
        out["instance_iam_role_arn"] = data["InstanceIamRoleArn"]
    return out
