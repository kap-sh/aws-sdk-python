"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#EncryptionContextMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_data_automation_runtime.types.encryption_context_key
    import capo_bedrock_data_automation_runtime.types.encryption_context_value

EncryptionContextMap: TypeAlias = dict[
    "capo_bedrock_data_automation_runtime.types.encryption_context_key.EncryptionContextKey",
    "capo_bedrock_data_automation_runtime.types.encryption_context_value.EncryptionContextValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: EncryptionContextMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> EncryptionContextMap:
    out: EncryptionContextMap = {}
    for key, value in data.items():
        out[key] = value
    return out
