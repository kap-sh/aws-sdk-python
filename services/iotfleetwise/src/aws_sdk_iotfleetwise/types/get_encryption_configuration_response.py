"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#GetEncryptionConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.encryption_status
    import aws_sdk_iotfleetwise.types.encryption_type
    import aws_sdk_iotfleetwise.types.error_message
    import aws_sdk_iotfleetwise.types.timestamp


class GetEncryptionConfigurationResponse(TypedDict):
    kms_key_id: NotRequired["str"]
    """<p>The ID of the KMS key that is used for encryption.</p>"""
    encryption_status: "aws_sdk_iotfleetwise.types.encryption_status.EncryptionStatus"
    """<p>The encryption status.</p>"""
    encryption_type: "aws_sdk_iotfleetwise.types.encryption_type.EncryptionType"
    """<p>The type of encryption. Set to <code>KMS_BASED_ENCRYPTION</code> to use a KMS key that you own and manage. Set to <code>FLEETWISE_DEFAULT_ENCRYPTION</code> to use an Amazon Web Services managed key that is owned by the Amazon Web Services IoT FleetWise service account.</p>"""
    error_message: NotRequired["aws_sdk_iotfleetwise.types.error_message.errorMessage"]
    """<p>The error message that describes why encryption settings couldn't be configured, if applicable.</p>"""
    creation_time: NotRequired["aws_sdk_iotfleetwise.types.timestamp.timestamp"]
    """<p>The time when encryption was configured in seconds since epoch (January 1, 1970 at midnight UTC time).</p>"""
    last_modification_time: NotRequired[
        "aws_sdk_iotfleetwise.types.timestamp.timestamp"
    ]
    """<p>The time when encryption was last updated in seconds since epoch (January 1, 1970 at midnight UTC time).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEncryptionConfigurationResponse) -> dict:
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
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "creation_time" in value:
        import aws_sdk_iotfleetwise.types.timestamp

        out["creationTime"] = (
            aws_sdk_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
                value["creation_time"]
            )
        )
    if "last_modification_time" in value:
        import aws_sdk_iotfleetwise.types.timestamp

        out["lastModificationTime"] = (
            aws_sdk_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
                value["last_modification_time"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEncryptionConfigurationResponse:
    out: GetEncryptionConfigurationResponse = {}  # type: ignore[typeddict-item]
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
            "GetEncryptionConfigurationResponse.encryption_status required"
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
            "GetEncryptionConfigurationResponse.encryption_type required"
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    if "creationTime" in data:
        import aws_sdk_iotfleetwise.types.timestamp

        out["creation_time"] = (
            aws_sdk_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["creationTime"]
            )
        )
    if "lastModificationTime" in data:
        import aws_sdk_iotfleetwise.types.timestamp

        out["last_modification_time"] = (
            aws_sdk_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["lastModificationTime"]
            )
        )
    return out
