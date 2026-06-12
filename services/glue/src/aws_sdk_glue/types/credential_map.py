"""Generated from Smithy shape ``com.amazonaws.glue#CredentialMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.credential_key
    import aws_sdk_glue.types.credential_value

CredentialMap: TypeAlias = dict[
    "aws_sdk_glue.types.credential_key.CredentialKey",
    "aws_sdk_glue.types.credential_value.CredentialValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: CredentialMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> CredentialMap:
    out: CredentialMap = {}
    for key, value in data.items():
        out[key] = value
    return out
