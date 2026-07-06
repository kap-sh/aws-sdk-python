"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PutDefaultEncryptionConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.arn
    import aws_sdk_iotsitewise.types.configuration_status
    import aws_sdk_iotsitewise.types.encryption_type


class PutDefaultEncryptionConfigurationResponse(TypedDict, closed=True):
    encryption_type: "aws_sdk_iotsitewise.types.encryption_type.EncryptionType"
    """<p>The type of encryption used for the encryption configuration.</p>"""
    kms_key_arn: NotRequired["aws_sdk_iotsitewise.types.arn.ARN"]
    """<p>The Key ARN of the KMS key used for KMS encryption if you use <code>KMS_BASED_ENCRYPTION</code>.</p>"""
    configuration_status: (
        "aws_sdk_iotsitewise.types.configuration_status.ConfigurationStatus"
    )
    """<p>The status of the account configuration. This contains the <code>ConfigurationState</code>. If there is an error, it also contains the <code>ErrorDetails</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutDefaultEncryptionConfigurationResponse) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.encryption_type

    out["encryptionType"] = aws_sdk_iotsitewise.types.encryption_type.serialize_json(
        value["encryption_type"]
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    import aws_sdk_iotsitewise.types.configuration_status

    out["configurationStatus"] = (
        aws_sdk_iotsitewise.types.configuration_status.serialize_json(
            value["configuration_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutDefaultEncryptionConfigurationResponse:
    out: PutDefaultEncryptionConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "encryptionType" in data:
        import aws_sdk_iotsitewise.types.encryption_type

        out["encryption_type"] = (
            aws_sdk_iotsitewise.types.encryption_type.deserialize_json(
                data["encryptionType"]
            )
        )
    else:
        raise DeserializationError(
            "PutDefaultEncryptionConfigurationResponse.encryption_type required"
        )
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "configurationStatus" in data:
        import aws_sdk_iotsitewise.types.configuration_status

        out["configuration_status"] = (
            aws_sdk_iotsitewise.types.configuration_status.deserialize_json(
                data["configurationStatus"]
            )
        )
    else:
        raise DeserializationError(
            "PutDefaultEncryptionConfigurationResponse.configuration_status required"
        )
    return out
