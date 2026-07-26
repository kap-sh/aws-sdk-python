"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#Tags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.tag_key
    import capo_mwaa_serverless.types.tag_value

Tags: TypeAlias = dict[
    "capo_mwaa_serverless.types.tag_key.TagKey",
    "capo_mwaa_serverless.types.tag_value.TagValue",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: Tags) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> Tags:
    out: Tags = {}
    for key, value in data.items():
        out[key] = value
    return out
