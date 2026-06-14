"""Generated from Smithy shape ``com.amazonaws.devopsguru#KMSServerSideEncryptionIntegration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.kms_key_id
    import aws_sdk_devops_guru.types.opt_in_status
    import aws_sdk_devops_guru.types.server_side_encryption_type


class KMSServerSideEncryptionIntegration(TypedDict):
    kms_key_id: NotRequired["aws_sdk_devops_guru.types.kms_key_id.KMSKeyId"]
    r"""<p> Describes the specified KMS key. </p> <p>To specify a KMS key, use its key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix it with \"alias/\". If you specify a predefined Amazon Web Services alias (an Amazon Web Services alias with no key ID), Amazon Web Services KMS associates the alias with an Amazon Web Services managed key and returns its KeyId and Arn in the response. To specify a KMS key in a different Amazon Web Services account, you must use the key ARN or alias ARN.</p> <p>For example: </p> <p>Key ID: 1234abcd-12ab-34cd-56ef-1234567890ab</p> <p>Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</p> <p>Alias name: alias/ExampleAlias</p> <p>Alias ARN: arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias</p>"""
    opt_in_status: NotRequired["aws_sdk_devops_guru.types.opt_in_status.OptInStatus"]
    """<p> Specifies if DevOps Guru is enabled for customer managed keys. </p>"""
    type: NotRequired[
        "aws_sdk_devops_guru.types.server_side_encryption_type.ServerSideEncryptionType"
    ]
    """<p> The type of KMS key used. Customer managed keys are the KMS keys that you create. Amazon Web Services owned keys are keys that are owned and managed by DevOps Guru. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KMSServerSideEncryptionIntegration) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["KMSKeyId"] = value["kms_key_id"]
    if "opt_in_status" in value:
        import aws_sdk_devops_guru.types.opt_in_status

        out["OptInStatus"] = aws_sdk_devops_guru.types.opt_in_status.serialize_json(
            value["opt_in_status"]
        )
    if "type" in value:
        import aws_sdk_devops_guru.types.server_side_encryption_type

        out["Type"] = (
            aws_sdk_devops_guru.types.server_side_encryption_type.serialize_json(
                value["type"]
            )
        )
    return out


def deserialize_json(data: dict) -> KMSServerSideEncryptionIntegration:
    out: KMSServerSideEncryptionIntegration = {}  # type: ignore[typeddict-item]
    if "KMSKeyId" in data:
        out["kms_key_id"] = data["KMSKeyId"]
    if "OptInStatus" in data:
        import aws_sdk_devops_guru.types.opt_in_status

        out["opt_in_status"] = aws_sdk_devops_guru.types.opt_in_status.deserialize_json(
            data["OptInStatus"]
        )
    if "Type" in data:
        import aws_sdk_devops_guru.types.server_side_encryption_type

        out["type"] = (
            aws_sdk_devops_guru.types.server_side_encryption_type.deserialize_json(
                data["Type"]
            )
        )
    return out
