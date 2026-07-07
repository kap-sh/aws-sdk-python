"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DescribeInstanceAccessControlAttributeConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.instance_access_control_attribute_configuration
    import aws_sdk_sso_admin.types.instance_access_control_attribute_configuration_status
    import aws_sdk_sso_admin.types.instance_access_control_attribute_configuration_status_reason


class DescribeInstanceAccessControlAttributeConfigurationResponse(
    TypedDict, closed=True
):
    status: NotRequired[
        "aws_sdk_sso_admin.types.instance_access_control_attribute_configuration_status.InstanceAccessControlAttributeConfigurationStatus"
    ]
    """<p>The status of the attribute configuration process.</p>"""
    status_reason: NotRequired[
        "aws_sdk_sso_admin.types.instance_access_control_attribute_configuration_status_reason.InstanceAccessControlAttributeConfigurationStatusReason"
    ]
    """<p>Provides more details about the current status of the specified attribute.</p>"""
    instance_access_control_attribute_configuration: NotRequired[
        "aws_sdk_sso_admin.types.instance_access_control_attribute_configuration.InstanceAccessControlAttributeConfiguration"
    ]
    """<p>Gets the list of IAM Identity Center identity store attributes that have been added to your ABAC configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeInstanceAccessControlAttributeConfigurationResponse,
) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_sso_admin.types.instance_access_control_attribute_configuration_status

        out["Status"] = (
            aws_sdk_sso_admin.types.instance_access_control_attribute_configuration_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    if "instance_access_control_attribute_configuration" in value:
        import aws_sdk_sso_admin.types.instance_access_control_attribute_configuration

        out["InstanceAccessControlAttributeConfiguration"] = (
            aws_sdk_sso_admin.types.instance_access_control_attribute_configuration.serialize_aws_json_1_1(
                value["instance_access_control_attribute_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeInstanceAccessControlAttributeConfigurationResponse:
    out: DescribeInstanceAccessControlAttributeConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_sso_admin.types.instance_access_control_attribute_configuration_status

        out["status"] = (
            aws_sdk_sso_admin.types.instance_access_control_attribute_configuration_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusReason" in data:
        out["status_reason"] = data["StatusReason"]
    if "InstanceAccessControlAttributeConfiguration" in data:
        import aws_sdk_sso_admin.types.instance_access_control_attribute_configuration

        out["instance_access_control_attribute_configuration"] = (
            aws_sdk_sso_admin.types.instance_access_control_attribute_configuration.deserialize_aws_json_1_1(
                data["InstanceAccessControlAttributeConfiguration"]
            )
        )
    return out
