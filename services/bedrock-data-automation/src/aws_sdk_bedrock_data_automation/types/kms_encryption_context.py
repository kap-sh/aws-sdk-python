"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#KmsEncryptionContext``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.encryption_context_key
    import aws_sdk_bedrock_data_automation.types.encryption_context_value

KmsEncryptionContext: TypeAlias = dict[
    "aws_sdk_bedrock_data_automation.types.encryption_context_key.EncryptionContextKey",
    "aws_sdk_bedrock_data_automation.types.encryption_context_value.EncryptionContextValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: KmsEncryptionContext) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> KmsEncryptionContext:
    out: KmsEncryptionContext = {}
    for key, value in data.items():
        out[key] = value
    return out
