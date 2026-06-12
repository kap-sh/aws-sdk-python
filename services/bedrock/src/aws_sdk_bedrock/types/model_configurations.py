"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.model_configuration

ModelConfigurations: TypeAlias = list[
    "aws_sdk_bedrock.types.model_configuration.ModelConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ModelConfigurations) -> list:
    import aws_sdk_bedrock.types.model_configuration

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock.types.model_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> ModelConfigurations:
    import aws_sdk_bedrock.types.model_configuration

    out: ModelConfigurations = []
    for item in data:
        out.append(aws_sdk_bedrock.types.model_configuration.deserialize_json(item))
    return out
