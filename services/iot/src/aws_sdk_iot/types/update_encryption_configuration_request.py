"""Generated from Smithy shape ``com.amazonaws.iot#UpdateEncryptionConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.encryption_type
    import aws_sdk_iot.types.kms_access_role_arn
    import aws_sdk_iot.types.kms_key_arn


class UpdateEncryptionConfigurationRequest(TypedDict):
    encryption_type: "aws_sdk_iot.types.encryption_type.EncryptionType"
    """<p>The type of the KMS key.</p>"""
    kms_key_arn: NotRequired["aws_sdk_iot.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the customer managedKMS key.</p>"""
    kms_access_role_arn: NotRequired[
        "aws_sdk_iot.types.kms_access_role_arn.KmsAccessRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM role assumed by Amazon Web Services IoT Core to call KMS on behalf of the customer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEncryptionConfigurationRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.encryption_type

    out["encryptionType"] = aws_sdk_iot.types.encryption_type.serialize_json(
        value["encryption_type"]
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "kms_access_role_arn" in value:
        out["kmsAccessRoleArn"] = value["kms_access_role_arn"]
    return out


def deserialize_json(data: dict) -> UpdateEncryptionConfigurationRequest:
    out: UpdateEncryptionConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "encryptionType" in data:
        import aws_sdk_iot.types.encryption_type

        out["encryption_type"] = aws_sdk_iot.types.encryption_type.deserialize_json(
            data["encryptionType"]
        )
    else:
        raise DeserializationError(
            "UpdateEncryptionConfigurationRequest.encryption_type required"
        )
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "kmsAccessRoleArn" in data:
        out["kms_access_role_arn"] = data["kmsAccessRoleArn"]
    return out
