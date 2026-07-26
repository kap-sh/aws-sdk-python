"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#GenericMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.generic_string

GenericMap: TypeAlias = dict[
    "capo_mwaa_serverless.types.generic_string.GenericString",
    "capo_mwaa_serverless.types.generic_string.GenericString",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: GenericMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> GenericMap:
    out: GenericMap = {}
    for key, value in data.items():
        out[key] = value
    return out
