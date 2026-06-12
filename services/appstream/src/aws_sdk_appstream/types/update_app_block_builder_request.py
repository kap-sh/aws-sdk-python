"""Generated from Smithy shape ``com.amazonaws.appstream#UpdateAppBlockBuilderRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.access_endpoint_list
    import aws_sdk_appstream.types.app_block_builder_attributes
    import aws_sdk_appstream.types.arn
    import aws_sdk_appstream.types.boolean_object
    import aws_sdk_appstream.types.description
    import aws_sdk_appstream.types.display_name
    import aws_sdk_appstream.types.name
    import aws_sdk_appstream.types.platform_type
    import aws_sdk_appstream.types.string
    import aws_sdk_appstream.types.vpc_config


class UpdateAppBlockBuilderRequest(TypedDict):
    name: NotRequired["aws_sdk_appstream.types.name.Name"]
    """<p>The unique name for the app block builder.</p>"""
    description: NotRequired["aws_sdk_appstream.types.description.Description"]
    """<p>The description of the app block builder.</p>"""
    display_name: NotRequired["aws_sdk_appstream.types.display_name.DisplayName"]
    """<p>The display name of the app block builder.</p>"""
    platform: NotRequired["aws_sdk_appstream.types.platform_type.PlatformType"]
    """<p>The platform of the app block builder.</p> <p> <code>WINDOWS_SERVER_2019</code> is the only valid value.</p>"""
    instance_type: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The instance type to use when launching the app block builder. The following instance types are available:</p> <ul> <li> <p>stream.standard.small</p> </li> <li> <p>stream.standard.medium</p> </li> <li> <p>stream.standard.large</p> </li> <li> <p>stream.standard.xlarge</p> </li> <li> <p>stream.standard.2xlarge</p> </li> </ul>"""
    vpc_config: NotRequired["aws_sdk_appstream.types.vpc_config.VpcConfig"]
    """<p>The VPC configuration for the app block builder.</p> <p>App block builders require that you specify at least two subnets in different availability zones.</p>"""
    enable_default_internet_access: NotRequired[
        "aws_sdk_appstream.types.boolean_object.BooleanObject"
    ]
    """<p>Enables or disables default internet access for the app block builder.</p>"""
    iam_role_arn: NotRequired["aws_sdk_appstream.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role to apply to the app block builder. To assume a role, the app block builder calls the AWS Security Token Service (STS) <code>AssumeRole</code> API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. WorkSpaces Applications retrieves the temporary credentials and creates the <b>appstream_machine_role</b> credential profile on the instance.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html\">Using an IAM Role to Grant Permissions to Applications and Scripts Running on WorkSpaces Applications Streaming Instances</a> in the <i>Amazon WorkSpaces Applications Administration Guide</i>.</p>"""
    access_endpoints: NotRequired[
        "aws_sdk_appstream.types.access_endpoint_list.AccessEndpointList"
    ]
    """<p>The list of interface VPC endpoint (interface endpoint) objects. Administrators can connect to the app block builder only through the specified endpoints.</p>"""
    attributes_to_delete: NotRequired[
        "aws_sdk_appstream.types.app_block_builder_attributes.AppBlockBuilderAttributes"
    ]
    """<p>The attributes to delete from the app block builder.</p>"""
    disable_imdsv1: NotRequired["aws_sdk_appstream.types.boolean_object.BooleanObject"]
    """<p>Set to true to disable Instance Metadata Service Version 1 (IMDSv1) and enforce IMDSv2. Set to false to enable both IMDSv1 and IMDSv2.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAppBlockBuilderRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "platform" in value:
        import aws_sdk_appstream.types.platform_type

        out["Platform"] = aws_sdk_appstream.types.platform_type.serialize_aws_json_1_1(
            value["platform"]
        )
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "vpc_config" in value:
        import aws_sdk_appstream.types.vpc_config

        out["VpcConfig"] = aws_sdk_appstream.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "enable_default_internet_access" in value:
        out["EnableDefaultInternetAccess"] = value["enable_default_internet_access"]
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    if "access_endpoints" in value:
        import aws_sdk_appstream.types.access_endpoint_list

        out["AccessEndpoints"] = (
            aws_sdk_appstream.types.access_endpoint_list.serialize_aws_json_1_1(
                value["access_endpoints"]
            )
        )
    if "attributes_to_delete" in value:
        import aws_sdk_appstream.types.app_block_builder_attributes

        out["AttributesToDelete"] = (
            aws_sdk_appstream.types.app_block_builder_attributes.serialize_aws_json_1_1(
                value["attributes_to_delete"]
            )
        )
    if "disable_imdsv1" in value:
        out["DisableIMDSV1"] = value["disable_imdsv1"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAppBlockBuilderRequest:
    out: UpdateAppBlockBuilderRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "Platform" in data:
        import aws_sdk_appstream.types.platform_type

        out["platform"] = (
            aws_sdk_appstream.types.platform_type.deserialize_aws_json_1_1(
                data["Platform"]
            )
        )
    if "InstanceType" in data:
        out["instance_type"] = data["InstanceType"]
    if "VpcConfig" in data:
        import aws_sdk_appstream.types.vpc_config

        out["vpc_config"] = aws_sdk_appstream.types.vpc_config.deserialize_aws_json_1_1(
            data["VpcConfig"]
        )
    if "EnableDefaultInternetAccess" in data:
        out["enable_default_internet_access"] = data["EnableDefaultInternetAccess"]
    if "IamRoleArn" in data:
        out["iam_role_arn"] = data["IamRoleArn"]
    if "AccessEndpoints" in data:
        import aws_sdk_appstream.types.access_endpoint_list

        out["access_endpoints"] = (
            aws_sdk_appstream.types.access_endpoint_list.deserialize_aws_json_1_1(
                data["AccessEndpoints"]
            )
        )
    if "AttributesToDelete" in data:
        import aws_sdk_appstream.types.app_block_builder_attributes

        out["attributes_to_delete"] = (
            aws_sdk_appstream.types.app_block_builder_attributes.deserialize_aws_json_1_1(
                data["AttributesToDelete"]
            )
        )
    if "DisableIMDSV1" in data:
        out["disable_imdsv1"] = data["DisableIMDSV1"]
    return out
