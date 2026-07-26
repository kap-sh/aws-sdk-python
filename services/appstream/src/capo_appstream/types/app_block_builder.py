"""Generated from Smithy shape ``com.amazonaws.appstream#AppBlockBuilder``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.access_endpoint_list
    import capo_appstream.types.app_block_builder_platform_type
    import capo_appstream.types.app_block_builder_state
    import capo_appstream.types.app_block_builder_state_change_reason
    import capo_appstream.types.arn
    import capo_appstream.types.boolean_object
    import capo_appstream.types.resource_errors
    import capo_appstream.types.string
    import capo_appstream.types.timestamp
    import capo_appstream.types.vpc_config


class AppBlockBuilder(TypedDict, closed=True):
    arn: NotRequired["capo_appstream.types.arn.Arn"]
    """<p>The ARN of the app block builder.</p>"""
    name: NotRequired["capo_appstream.types.string.String"]
    """<p>The name of the app block builder.</p>"""
    display_name: NotRequired["capo_appstream.types.string.String"]
    """<p>The display name of the app block builder.</p>"""
    description: NotRequired["capo_appstream.types.string.String"]
    """<p>The description of the app block builder.</p>"""
    platform: NotRequired[
        "capo_appstream.types.app_block_builder_platform_type.AppBlockBuilderPlatformType"
    ]
    """<p>The platform of the app block builder.</p> <p> <code>WINDOWS_SERVER_2019</code> is the only valid value.</p>"""
    instance_type: NotRequired["capo_appstream.types.string.String"]
    """<p>The instance type of the app block builder.</p>"""
    enable_default_internet_access: NotRequired[
        "capo_appstream.types.boolean_object.BooleanObject"
    ]
    """<p>Indicates whether default internet access is enabled for the app block builder.</p>"""
    iam_role_arn: NotRequired["capo_appstream.types.arn.Arn"]
    """<p>The ARN of the IAM role that is applied to the app block builder.</p>"""
    vpc_config: NotRequired["capo_appstream.types.vpc_config.VpcConfig"]
    """<p>The VPC configuration for the app block builder.</p>"""
    state: NotRequired[
        "capo_appstream.types.app_block_builder_state.AppBlockBuilderState"
    ]
    """<p>The state of the app block builder.</p>"""
    created_time: NotRequired["capo_appstream.types.timestamp.Timestamp"]
    """<p>The creation time of the app block builder.</p>"""
    app_block_builder_errors: NotRequired[
        "capo_appstream.types.resource_errors.ResourceErrors"
    ]
    """<p>The app block builder errors.</p>"""
    state_change_reason: NotRequired[
        "capo_appstream.types.app_block_builder_state_change_reason.AppBlockBuilderStateChangeReason"
    ]
    """<p>The state change reason.</p>"""
    access_endpoints: NotRequired[
        "capo_appstream.types.access_endpoint_list.AccessEndpointList"
    ]
    """<p>The list of interface VPC endpoint (interface endpoint) objects. Administrators can connect to the app block builder only through the specified endpoints.</p>"""
    disable_imdsv1: NotRequired["capo_appstream.types.boolean_object.BooleanObject"]
    """<p>Indicates whether Instance Metadata Service Version 1 (IMDSv1) is disabled for the app block builder.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppBlockBuilder) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "platform" in value:
        import capo_appstream.types.app_block_builder_platform_type

        out["Platform"] = (
            capo_appstream.types.app_block_builder_platform_type.serialize_aws_json_1_1(
                value["platform"]
            )
        )
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "enable_default_internet_access" in value:
        out["EnableDefaultInternetAccess"] = value["enable_default_internet_access"]
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    if "vpc_config" in value:
        import capo_appstream.types.vpc_config

        out["VpcConfig"] = capo_appstream.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "state" in value:
        import capo_appstream.types.app_block_builder_state

        out["State"] = (
            capo_appstream.types.app_block_builder_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "created_time" in value:
        import capo_appstream.types.timestamp

        out["CreatedTime"] = capo_appstream.types.timestamp.serialize_aws_json_1_1(
            value["created_time"]
        )
    if "app_block_builder_errors" in value:
        import capo_appstream.types.resource_errors

        out["AppBlockBuilderErrors"] = (
            capo_appstream.types.resource_errors.serialize_aws_json_1_1(
                value["app_block_builder_errors"]
            )
        )
    if "state_change_reason" in value:
        import capo_appstream.types.app_block_builder_state_change_reason

        out["StateChangeReason"] = (
            capo_appstream.types.app_block_builder_state_change_reason.serialize_aws_json_1_1(
                value["state_change_reason"]
            )
        )
    if "access_endpoints" in value:
        import capo_appstream.types.access_endpoint_list

        out["AccessEndpoints"] = (
            capo_appstream.types.access_endpoint_list.serialize_aws_json_1_1(
                value["access_endpoints"]
            )
        )
    if "disable_imdsv1" in value:
        out["DisableIMDSV1"] = value["disable_imdsv1"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AppBlockBuilder:
    out: AppBlockBuilder = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Platform" in data:
        import capo_appstream.types.app_block_builder_platform_type

        out["platform"] = (
            capo_appstream.types.app_block_builder_platform_type.deserialize_aws_json_1_1(
                data["Platform"]
            )
        )
    if "InstanceType" in data:
        out["instance_type"] = data["InstanceType"]
    if "EnableDefaultInternetAccess" in data:
        out["enable_default_internet_access"] = data["EnableDefaultInternetAccess"]
    if "IamRoleArn" in data:
        out["iam_role_arn"] = data["IamRoleArn"]
    if "VpcConfig" in data:
        import capo_appstream.types.vpc_config

        out["vpc_config"] = capo_appstream.types.vpc_config.deserialize_aws_json_1_1(
            data["VpcConfig"]
        )
    if "State" in data:
        import capo_appstream.types.app_block_builder_state

        out["state"] = (
            capo_appstream.types.app_block_builder_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if "CreatedTime" in data:
        import capo_appstream.types.timestamp

        out["created_time"] = capo_appstream.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedTime"]
        )
    if "AppBlockBuilderErrors" in data:
        import capo_appstream.types.resource_errors

        out["app_block_builder_errors"] = (
            capo_appstream.types.resource_errors.deserialize_aws_json_1_1(
                data["AppBlockBuilderErrors"]
            )
        )
    if "StateChangeReason" in data:
        import capo_appstream.types.app_block_builder_state_change_reason

        out["state_change_reason"] = (
            capo_appstream.types.app_block_builder_state_change_reason.deserialize_aws_json_1_1(
                data["StateChangeReason"]
            )
        )
    if "AccessEndpoints" in data:
        import capo_appstream.types.access_endpoint_list

        out["access_endpoints"] = (
            capo_appstream.types.access_endpoint_list.deserialize_aws_json_1_1(
                data["AccessEndpoints"]
            )
        )
    if "DisableIMDSV1" in data:
        out["disable_imdsv1"] = data["DisableIMDSV1"]
    return out
