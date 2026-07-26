"""Generated from Smithy shape ``com.amazonaws.ecs#LogConfigurationOptionsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.string

LogConfigurationOptionsMap: TypeAlias = dict[
    "capo_ecs.types.string.String", "capo_ecs.types.string.String"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: LogConfigurationOptionsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> LogConfigurationOptionsMap:
    out: LogConfigurationOptionsMap = {}
    for key, value in data.items():
        out[key] = value
    return out
