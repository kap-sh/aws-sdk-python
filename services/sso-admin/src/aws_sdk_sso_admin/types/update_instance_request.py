"""Generated from Smithy shape ``com.amazonaws.ssoadmin#UpdateInstanceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.encryption_configuration
    import aws_sdk_sso_admin.types.instance_arn
    import aws_sdk_sso_admin.types.name_type


class UpdateInstanceRequest(TypedDict):
    name: NotRequired["aws_sdk_sso_admin.types.name_type.NameType"]
    """<p>Updates the instance name.</p>"""
    instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn"
    """<p>The ARN of the instance of IAM Identity Center under which the operation will run. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    encryption_configuration: NotRequired[
        "aws_sdk_sso_admin.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>Specifies the encryption configuration for your IAM Identity Center instance. You can use this to configure customer managed KMS keys or Amazon Web Services owned KMS keys for encrypting your instance data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateInstanceRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    out["InstanceArn"] = value["instance_arn"]
    if "encryption_configuration" in value:
        import aws_sdk_sso_admin.types.encryption_configuration

        out["EncryptionConfiguration"] = (
            aws_sdk_sso_admin.types.encryption_configuration.serialize_aws_json_1_1(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateInstanceRequest:
    out: UpdateInstanceRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError("UpdateInstanceRequest.instance_arn required")
    if "EncryptionConfiguration" in data:
        import aws_sdk_sso_admin.types.encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_sso_admin.types.encryption_configuration.deserialize_aws_json_1_1(
                data["EncryptionConfiguration"]
            )
        )
    return out
