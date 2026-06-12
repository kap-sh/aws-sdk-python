"""Generated from Smithy shape ``com.amazonaws.glue#IntegrationAdditionalEncryptionContextMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.integration_string

IntegrationAdditionalEncryptionContextMap: TypeAlias = dict[
    "aws_sdk_glue.types.integration_string.IntegrationString",
    "aws_sdk_glue.types.integration_string.IntegrationString",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    input_to_serialize: IntegrationAdditionalEncryptionContextMap,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> IntegrationAdditionalEncryptionContextMap:
    out: IntegrationAdditionalEncryptionContextMap = {}
    for key, value in data.items():
        out[key] = value
    return out
