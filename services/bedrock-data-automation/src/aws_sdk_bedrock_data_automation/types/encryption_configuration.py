"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#EncryptionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.kms_encryption_context
    import aws_sdk_bedrock_data_automation.types.kms_key_id


class EncryptionConfiguration(TypedDict):
    kms_key_id: "aws_sdk_bedrock_data_automation.types.kms_key_id.KmsKeyId"
    kms_encryption_context: NotRequired[
        "aws_sdk_bedrock_data_automation.types.kms_encryption_context.KmsEncryptionContext"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionConfiguration) -> dict:
    out: dict = {}
    out["kmsKeyId"] = value["kms_key_id"]
    if "kms_encryption_context" in value:
        import aws_sdk_bedrock_data_automation.types.kms_encryption_context

        out["kmsEncryptionContext"] = (
            aws_sdk_bedrock_data_automation.types.kms_encryption_context.serialize_json(
                value["kms_encryption_context"]
            )
        )
    return out


def deserialize_json(data: dict) -> EncryptionConfiguration:
    out: EncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    else:
        raise DeserializationError("EncryptionConfiguration.kms_key_id required")
    if "kmsEncryptionContext" in data:
        import aws_sdk_bedrock_data_automation.types.kms_encryption_context

        out["kms_encryption_context"] = (
            aws_sdk_bedrock_data_automation.types.kms_encryption_context.deserialize_json(
                data["kmsEncryptionContext"]
            )
        )
    return out
