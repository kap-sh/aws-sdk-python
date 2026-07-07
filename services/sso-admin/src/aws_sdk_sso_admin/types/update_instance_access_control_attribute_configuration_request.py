"""Generated from Smithy shape ``com.amazonaws.ssoadmin#UpdateInstanceAccessControlAttributeConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.instance_access_control_attribute_configuration
    import aws_sdk_sso_admin.types.instance_arn


class UpdateInstanceAccessControlAttributeConfigurationRequest(TypedDict, closed=True):
    instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn"
    """<p>The ARN of the IAM Identity Center instance under which the operation will be executed.</p>"""
    instance_access_control_attribute_configuration: "aws_sdk_sso_admin.types.instance_access_control_attribute_configuration.InstanceAccessControlAttributeConfiguration"
    """<p>Updates the attributes for your ABAC configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: UpdateInstanceAccessControlAttributeConfigurationRequest,
) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    import aws_sdk_sso_admin.types.instance_access_control_attribute_configuration

    out["InstanceAccessControlAttributeConfiguration"] = (
        aws_sdk_sso_admin.types.instance_access_control_attribute_configuration.serialize_aws_json_1_1(
            value["instance_access_control_attribute_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> UpdateInstanceAccessControlAttributeConfigurationRequest:
    out: UpdateInstanceAccessControlAttributeConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError(
            "UpdateInstanceAccessControlAttributeConfigurationRequest.instance_arn required"
        )
    if "InstanceAccessControlAttributeConfiguration" in data:
        import aws_sdk_sso_admin.types.instance_access_control_attribute_configuration

        out["instance_access_control_attribute_configuration"] = (
            aws_sdk_sso_admin.types.instance_access_control_attribute_configuration.deserialize_aws_json_1_1(
                data["InstanceAccessControlAttributeConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateInstanceAccessControlAttributeConfigurationRequest.instance_access_control_attribute_configuration required"
        )
    return out
