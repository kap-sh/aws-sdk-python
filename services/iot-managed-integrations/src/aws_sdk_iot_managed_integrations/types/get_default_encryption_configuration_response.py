"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetDefaultEncryptionConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.configuration_status
    import aws_sdk_iot_managed_integrations.types.encryption_type
    import aws_sdk_iot_managed_integrations.types.kms_key_arn


class GetDefaultEncryptionConfigurationResponse(TypedDict, closed=True):
    configuration_status: "aws_sdk_iot_managed_integrations.types.configuration_status.ConfigurationStatus"
    """<p>Provides the status of the default encryption configuration for an Amazon Web Services account.</p>"""
    encryption_type: (
        "aws_sdk_iot_managed_integrations.types.encryption_type.EncryptionType"
    )
    """<p>The type of encryption used for the encryption configuration.</p>"""
    kms_key_arn: NotRequired[
        "aws_sdk_iot_managed_integrations.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The Key Amazon Resource Name (ARN) of the AWS KMS key used for KMS encryption if you use <code>KMS_BASED_ENCRYPTION</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDefaultEncryptionConfigurationResponse) -> dict:
    out: dict = {}
    import aws_sdk_iot_managed_integrations.types.configuration_status

    out["configurationStatus"] = (
        aws_sdk_iot_managed_integrations.types.configuration_status.serialize_json(
            value["configuration_status"]
        )
    )
    import aws_sdk_iot_managed_integrations.types.encryption_type

    out["encryptionType"] = (
        aws_sdk_iot_managed_integrations.types.encryption_type.serialize_json(
            value["encryption_type"]
        )
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> GetDefaultEncryptionConfigurationResponse:
    out: GetDefaultEncryptionConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "configurationStatus" in data:
        import aws_sdk_iot_managed_integrations.types.configuration_status

        out["configuration_status"] = (
            aws_sdk_iot_managed_integrations.types.configuration_status.deserialize_json(
                data["configurationStatus"]
            )
        )
    else:
        raise DeserializationError(
            "GetDefaultEncryptionConfigurationResponse.configuration_status required"
        )
    if "encryptionType" in data:
        import aws_sdk_iot_managed_integrations.types.encryption_type

        out["encryption_type"] = (
            aws_sdk_iot_managed_integrations.types.encryption_type.deserialize_json(
                data["encryptionType"]
            )
        )
    else:
        raise DeserializationError(
            "GetDefaultEncryptionConfigurationResponse.encryption_type required"
        )
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
