"""Generated from Smithy shape ``com.amazonaws.codepipeline#ResolvedRuleConfigurationMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.string

ResolvedRuleConfigurationMap: TypeAlias = dict[
    "capo_codepipeline.types.string.String", "capo_codepipeline.types.string.String"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ResolvedRuleConfigurationMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ResolvedRuleConfigurationMap:
    out: ResolvedRuleConfigurationMap = {}
    for key, value in data.items():
        out[key] = value
    return out
