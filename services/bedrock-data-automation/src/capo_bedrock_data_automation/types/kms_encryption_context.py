"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#KmsEncryptionContext``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.encryption_context_key
    import capo_bedrock_data_automation.types.encryption_context_value

KmsEncryptionContext: TypeAlias = dict[
    "capo_bedrock_data_automation.types.encryption_context_key.EncryptionContextKey",
    "capo_bedrock_data_automation.types.encryption_context_value.EncryptionContextValue",
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
        if value is None:
            continue
        out[key] = value
    return out
