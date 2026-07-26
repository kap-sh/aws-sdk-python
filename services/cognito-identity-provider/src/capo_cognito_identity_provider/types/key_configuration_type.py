"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#KeyConfigurationType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.encryption_key_arn_type
    import capo_cognito_identity_provider.types.encryption_key_type


class KeyConfigurationType(TypedDict, closed=True):
    key_type: NotRequired[
        "capo_cognito_identity_provider.types.encryption_key_type.EncryptionKeyType"
    ]
    """<p>The type of encryption key used for the user pool.</p> <dl> <dt>AWS_OWNED_KEY</dt> <dd> <p>A key owned by Amazon Web Services in Key Management Service.</p> </dd> <dt>CUSTOMER_MANAGED_KEY</dt> <dd> <p>A key managed by the customer in Key Management Service. You must use a multi-region key to enable multi-region replication for a user pool.</p> </dd> </dl>"""
    kms_key_arn: NotRequired[
        "capo_cognito_identity_provider.types.encryption_key_arn_type.EncryptionKeyArnType"
    ]
    """<p>The Amazon Resource Name (ARN) of the KMS key used for encryption. If not specified, Amazon Web Services managed keys are used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyConfigurationType) -> dict:
    out: dict = {}
    if "key_type" in value:
        import capo_cognito_identity_provider.types.encryption_key_type

        out["KeyType"] = (
            capo_cognito_identity_provider.types.encryption_key_type.serialize_aws_json_1_1(
                value["key_type"]
            )
        )
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KeyConfigurationType:
    out: KeyConfigurationType = {}  # type: ignore[typeddict-item]
    if "KeyType" in data:
        import capo_cognito_identity_provider.types.encryption_key_type

        out["key_type"] = (
            capo_cognito_identity_provider.types.encryption_key_type.deserialize_aws_json_1_1(
                data["KeyType"]
            )
        )
    if "KmsKeyArn" in data:
        out["kms_key_arn"] = data["KmsKeyArn"]
    return out
