"""Generated from Smithy shape ``com.amazonaws.codepipeline#ResolvedActionConfigurationMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.string

ResolvedActionConfigurationMap: TypeAlias = dict[
    "aws_sdk_codepipeline.types.string.String",
    "aws_sdk_codepipeline.types.string.String",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ResolvedActionConfigurationMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ResolvedActionConfigurationMap:
    out: ResolvedActionConfigurationMap = {}
    for key, value in data.items():
        out[key] = value
    return out
