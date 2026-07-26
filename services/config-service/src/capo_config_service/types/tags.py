"""Generated from Smithy shape ``com.amazonaws.configservice#Tags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.name
    import capo_config_service.types.value

Tags: TypeAlias = dict[
    "capo_config_service.types.name.Name", "capo_config_service.types.value.Value"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: Tags) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> Tags:
    out: Tags = {}
    for key, value in data.items():
        out[key] = value
    return out
