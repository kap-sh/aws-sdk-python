"""Generated from Smithy shape ``com.amazonaws.transcribe#KMSEncryptionContextMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.non_empty_string

KMSEncryptionContextMap: TypeAlias = dict[
    "aws_sdk_transcribe.types.non_empty_string.NonEmptyString",
    "aws_sdk_transcribe.types.non_empty_string.NonEmptyString",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: KMSEncryptionContextMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> KMSEncryptionContextMap:
    out: KMSEncryptionContextMap = {}
    for key, value in data.items():
        out[key] = value
    return out
