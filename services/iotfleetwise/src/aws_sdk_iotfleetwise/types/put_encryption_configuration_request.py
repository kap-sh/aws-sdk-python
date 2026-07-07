"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#PutEncryptionConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.encryption_type


class PutEncryptionConfigurationRequest(TypedDict, closed=True):
    kms_key_id: NotRequired["str"]
    """<p>The ID of the KMS key that is used for encryption.</p>"""
    encryption_type: "aws_sdk_iotfleetwise.types.encryption_type.EncryptionType"
    """<p>The type of encryption. Choose <code>KMS_BASED_ENCRYPTION</code> to use a KMS key or <code>FLEETWISE_DEFAULT_ENCRYPTION</code> to use an Amazon Web Services managed key.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutEncryptionConfigurationRequest) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    import aws_sdk_iotfleetwise.types.encryption_type

    out["encryptionType"] = (
        aws_sdk_iotfleetwise.types.encryption_type.serialize_aws_json_1_0(
            value["encryption_type"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> PutEncryptionConfigurationRequest:
    out: PutEncryptionConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "encryptionType" in data:
        import aws_sdk_iotfleetwise.types.encryption_type

        out["encryption_type"] = (
            aws_sdk_iotfleetwise.types.encryption_type.deserialize_aws_json_1_0(
                data["encryptionType"]
            )
        )
    else:
        raise DeserializationError(
            "PutEncryptionConfigurationRequest.encryption_type required"
        )
    return out
