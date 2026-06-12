"""Generated from Smithy shape ``com.amazonaws.sagemaker#QueryProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.string256

QueryProperties: TypeAlias = dict[
    "aws_sdk_sagemaker.types.string256.String256",
    "aws_sdk_sagemaker.types.string256.String256",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: QueryProperties) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryProperties:
    out: QueryProperties = {}
    for key, value in data.items():
        out[key] = value
    return out
