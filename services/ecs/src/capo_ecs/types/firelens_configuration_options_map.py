"""Generated from Smithy shape ``com.amazonaws.ecs#FirelensConfigurationOptionsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.string

FirelensConfigurationOptionsMap: TypeAlias = dict[
    "capo_ecs.types.string.String", "capo_ecs.types.string.String"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: FirelensConfigurationOptionsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> FirelensConfigurationOptionsMap:
    out: FirelensConfigurationOptionsMap = {}
    for key, value in data.items():
        out[key] = value
    return out
