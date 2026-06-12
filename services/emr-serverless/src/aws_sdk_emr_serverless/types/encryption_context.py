"""Generated from Smithy shape ``com.amazonaws.emrserverless#EncryptionContext``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.encryption_context_key
    import aws_sdk_emr_serverless.types.encryption_context_value

EncryptionContext: TypeAlias = dict[
    "aws_sdk_emr_serverless.types.encryption_context_key.EncryptionContextKey",
    "aws_sdk_emr_serverless.types.encryption_context_value.EncryptionContextValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: EncryptionContext) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> EncryptionContext:
    out: EncryptionContext = {}
    for key, value in data.items():
        out[key] = value
    return out
