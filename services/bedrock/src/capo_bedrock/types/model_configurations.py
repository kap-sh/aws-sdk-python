"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.model_configuration

ModelConfigurations: TypeAlias = list[
    "capo_bedrock.types.model_configuration.ModelConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ModelConfigurations) -> list:
    import capo_bedrock.types.model_configuration

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.model_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> ModelConfigurations:
    import capo_bedrock.types.model_configuration

    out: ModelConfigurations = []
    for item in data:
        out.append(capo_bedrock.types.model_configuration.deserialize_json(item))
    return out
