"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#EncryptionContext``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.encryption_context_key
    import aws_sdk_verifiedpermissions.types.encryption_context_value

EncryptionContext: TypeAlias = dict["aws_sdk_verifiedpermissions.types.encryption_context_key.EncryptionContextKey", "aws_sdk_verifiedpermissions.types.encryption_context_value.EncryptionContextValue"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: EncryptionContext) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> EncryptionContext:
    out: EncryptionContext = {}
    for key, value in data.items():
        out[key] = value
    return out