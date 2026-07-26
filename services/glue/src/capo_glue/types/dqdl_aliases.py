"""Generated from Smithy shape ``com.amazonaws.glue#DQDLAliases``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.node_name

DQDLAliases: TypeAlias = dict[
    "capo_glue.types.node_name.NodeName",
    "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: DQDLAliases) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> DQDLAliases:
    out: DQDLAliases = {}
    for key, value in data.items():
        out[key] = value
    return out
