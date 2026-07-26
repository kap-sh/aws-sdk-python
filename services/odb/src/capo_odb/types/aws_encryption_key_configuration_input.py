"""Generated from Smithy shape ``com.amazonaws.odb#AwsEncryptionKeyConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.external_id_type
    import capo_odb.types.kms_key_id_or_arn
    import capo_odb.types.role_arn


class AwsEncryptionKeyConfigurationInput(TypedDict, closed=True):
    iam_role_arn: NotRequired["capo_odb.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Identity and Access Management (IAM) role that grants access to the KMS key.</p>"""
    external_id_type: NotRequired["capo_odb.types.external_id_type.ExternalIdType"]
    """<p>The type of external identifier associated with the encryption key.</p>"""
    kms_key_id: NotRequired["capo_odb.types.kms_key_id_or_arn.KmsKeyIdOrArn"]
    """<p>The identifier or ARN of the Amazon Web Services KMS key to use for encryption.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsEncryptionKeyConfigurationInput) -> dict:
    out: dict = {}
    if "iam_role_arn" in value:
        out["iamRoleArn"] = value["iam_role_arn"]
    if "external_id_type" in value:
        import capo_odb.types.external_id_type

        out["externalIdType"] = capo_odb.types.external_id_type.serialize_aws_json_1_0(
            value["external_id_type"]
        )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AwsEncryptionKeyConfigurationInput:
    out: AwsEncryptionKeyConfigurationInput = {}  # type: ignore[typeddict-item]
    if "iamRoleArn" in data:
        out["iam_role_arn"] = data["iamRoleArn"]
    if "externalIdType" in data:
        import capo_odb.types.external_id_type

        out["external_id_type"] = (
            capo_odb.types.external_id_type.deserialize_aws_json_1_0(
                data["externalIdType"]
            )
        )
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    return out
