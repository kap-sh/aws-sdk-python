"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#PutEncryptionConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.encryption_status
    import aws_sdk_iotfleetwise.types.encryption_type


class PutEncryptionConfigurationResponse(TypedDict, closed=True):
    kms_key_id: NotRequired["str"]
    """<p>The ID of the KMS key that is used for encryption.</p>"""
    encryption_status: "aws_sdk_iotfleetwise.types.encryption_status.EncryptionStatus"
    """<p>The encryption status.</p>"""
    encryption_type: "aws_sdk_iotfleetwise.types.encryption_type.EncryptionType"
    """<p>The type of encryption. Set to <code>KMS_BASED_ENCRYPTION</code> to use an KMS key that you own and manage. Set to <code>FLEETWISE_DEFAULT_ENCRYPTION</code> to use an Amazon Web Services managed key that is owned by the Amazon Web Services IoT FleetWise service account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutEncryptionConfigurationResponse) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    import aws_sdk_iotfleetwise.types.encryption_status

    out["encryptionStatus"] = (
        aws_sdk_iotfleetwise.types.encryption_status.serialize_aws_json_1_0(
            value["encryption_status"]
        )
    )
    import aws_sdk_iotfleetwise.types.encryption_type

    out["encryptionType"] = (
        aws_sdk_iotfleetwise.types.encryption_type.serialize_aws_json_1_0(
            value["encryption_type"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> PutEncryptionConfigurationResponse:
    out: PutEncryptionConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "encryptionStatus" in data:
        import aws_sdk_iotfleetwise.types.encryption_status

        out["encryption_status"] = (
            aws_sdk_iotfleetwise.types.encryption_status.deserialize_aws_json_1_0(
                data["encryptionStatus"]
            )
        )
    else:
        raise DeserializationError(
            "PutEncryptionConfigurationResponse.encryption_status required"
        )
    if "encryptionType" in data:
        import aws_sdk_iotfleetwise.types.encryption_type

        out["encryption_type"] = (
            aws_sdk_iotfleetwise.types.encryption_type.deserialize_aws_json_1_0(
                data["encryptionType"]
            )
        )
    else:
        raise DeserializationError(
            "PutEncryptionConfigurationResponse.encryption_type required"
        )
    return out
