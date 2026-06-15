"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RatingScale``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.categorical_scale_definitions
    import aws_sdk_bedrock_agentcore_control.types.numerical_scale_definitions


class _RatingScale_numerical(TypedDict):
    numerical: "aws_sdk_bedrock_agentcore_control.types.numerical_scale_definitions.NumericalScaleDefinitions"


class _RatingScale_categorical(TypedDict):
    categorical: "aws_sdk_bedrock_agentcore_control.types.categorical_scale_definitions.CategoricalScaleDefinitions"


RatingScale: TypeAlias = _RatingScale_numerical | _RatingScale_categorical


# --- restJson1 ser/de ---
def serialize_json(value: RatingScale) -> dict:
    if "numerical" in value:
        import aws_sdk_bedrock_agentcore_control.types.numerical_scale_definitions

        return {
            "numerical": aws_sdk_bedrock_agentcore_control.types.numerical_scale_definitions.serialize_json(
                value["numerical"]
            )
        }
    elif "categorical" in value:
        import aws_sdk_bedrock_agentcore_control.types.categorical_scale_definitions

        return {
            "categorical": aws_sdk_bedrock_agentcore_control.types.categorical_scale_definitions.serialize_json(
                value["categorical"]
            )
        }
    else:
        raise SerializationError("RatingScale: no variant present")


def deserialize_json(data: dict) -> RatingScale:
    if "numerical" in data:
        import aws_sdk_bedrock_agentcore_control.types.numerical_scale_definitions

        return {
            "numerical": aws_sdk_bedrock_agentcore_control.types.numerical_scale_definitions.deserialize_json(
                data["numerical"]
            )
        }
    elif "categorical" in data:
        import aws_sdk_bedrock_agentcore_control.types.categorical_scale_definitions

        return {
            "categorical": aws_sdk_bedrock_agentcore_control.types.categorical_scale_definitions.deserialize_json(
                data["categorical"]
            )
        }
    else:
        raise DeserializationError("RatingScale: no recognized variant key")
