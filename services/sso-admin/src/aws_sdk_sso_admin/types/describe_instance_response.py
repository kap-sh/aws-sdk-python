"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DescribeInstanceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.account_id
    import aws_sdk_sso_admin.types.date
    import aws_sdk_sso_admin.types.encryption_configuration_details
    import aws_sdk_sso_admin.types.id
    import aws_sdk_sso_admin.types.instance_arn
    import aws_sdk_sso_admin.types.instance_status
    import aws_sdk_sso_admin.types.name_type
    import aws_sdk_sso_admin.types.reason


class DescribeInstanceResponse(TypedDict):
    instance_arn: NotRequired["aws_sdk_sso_admin.types.instance_arn.InstanceArn"]
    r"""<p>The ARN of the instance of IAM Identity Center under which the operation will run. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    identity_store_id: NotRequired["aws_sdk_sso_admin.types.id.Id"]
    """<p>The identifier of the identity store that is connected to the instance of IAM Identity Center.</p>"""
    owner_account_id: NotRequired["aws_sdk_sso_admin.types.account_id.AccountId"]
    """<p>The identifier of the Amazon Web Services account for which the instance was created.</p>"""
    name: NotRequired["aws_sdk_sso_admin.types.name_type.NameType"]
    """<p>Specifies the instance name.</p>"""
    created_date: NotRequired["aws_sdk_sso_admin.types.date.Date"]
    """<p>The date the instance was created.</p>"""
    status: NotRequired["aws_sdk_sso_admin.types.instance_status.InstanceStatus"]
    """<p>The status of the instance. </p>"""
    status_reason: NotRequired["aws_sdk_sso_admin.types.reason.Reason"]
    """<p>Provides additional context about the current status of the IAM Identity Center instance. This field is particularly useful when an instance is in a non-ACTIVE state, such as CREATE_FAILED. When an instance fails to create or update, this field contains information about the cause, which may include issues with KMS key configuration, permission problems with the specified KMS key, or service-related errors. </p>"""
    encryption_configuration_details: NotRequired[
        "aws_sdk_sso_admin.types.encryption_configuration_details.EncryptionConfigurationDetails"
    ]
    """<p>Contains the encryption configuration for your IAM Identity Center instance, including the encryption status, KMS key type, and KMS key ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeInstanceResponse) -> dict:
    out: dict = {}
    if "instance_arn" in value:
        out["InstanceArn"] = value["instance_arn"]
    if "identity_store_id" in value:
        out["IdentityStoreId"] = value["identity_store_id"]
    if "owner_account_id" in value:
        out["OwnerAccountId"] = value["owner_account_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "created_date" in value:
        import aws_sdk_sso_admin.types.date

        out["CreatedDate"] = aws_sdk_sso_admin.types.date.serialize_aws_json_1_1(
            value["created_date"]
        )
    if "status" in value:
        import aws_sdk_sso_admin.types.instance_status

        out["Status"] = aws_sdk_sso_admin.types.instance_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    if "encryption_configuration_details" in value:
        import aws_sdk_sso_admin.types.encryption_configuration_details

        out["EncryptionConfigurationDetails"] = (
            aws_sdk_sso_admin.types.encryption_configuration_details.serialize_aws_json_1_1(
                value["encryption_configuration_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeInstanceResponse:
    out: DescribeInstanceResponse = {}  # type: ignore[typeddict-item]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    if "IdentityStoreId" in data:
        out["identity_store_id"] = data["IdentityStoreId"]
    if "OwnerAccountId" in data:
        out["owner_account_id"] = data["OwnerAccountId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "CreatedDate" in data:
        import aws_sdk_sso_admin.types.date

        out["created_date"] = aws_sdk_sso_admin.types.date.deserialize_aws_json_1_1(
            data["CreatedDate"]
        )
    if "Status" in data:
        import aws_sdk_sso_admin.types.instance_status

        out["status"] = (
            aws_sdk_sso_admin.types.instance_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusReason" in data:
        out["status_reason"] = data["StatusReason"]
    if "EncryptionConfigurationDetails" in data:
        import aws_sdk_sso_admin.types.encryption_configuration_details

        out["encryption_configuration_details"] = (
            aws_sdk_sso_admin.types.encryption_configuration_details.deserialize_aws_json_1_1(
                data["EncryptionConfigurationDetails"]
            )
        )
    return out
