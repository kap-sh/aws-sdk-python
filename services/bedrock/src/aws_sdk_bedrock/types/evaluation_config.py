"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_evaluation_config
    import aws_sdk_bedrock.types.human_evaluation_config


class _EvaluationConfig_automated(TypedDict, closed=True):
    automated: (
        "aws_sdk_bedrock.types.automated_evaluation_config.AutomatedEvaluationConfig"
    )


class _EvaluationConfig_human(TypedDict, closed=True):
    human: "aws_sdk_bedrock.types.human_evaluation_config.HumanEvaluationConfig"


EvaluationConfig: TypeAlias = _EvaluationConfig_automated | _EvaluationConfig_human


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationConfig) -> dict:
    if "automated" in value:
        import aws_sdk_bedrock.types.automated_evaluation_config

        return {
            "automated": aws_sdk_bedrock.types.automated_evaluation_config.serialize_json(
                value["automated"]
            )
        }
    elif "human" in value:
        import aws_sdk_bedrock.types.human_evaluation_config

        return {
            "human": aws_sdk_bedrock.types.human_evaluation_config.serialize_json(
                value["human"]
            )
        }
    else:
        raise SerializationError("EvaluationConfig: no variant present")


def deserialize_json(data: dict) -> EvaluationConfig:
    if "automated" in data:
        import aws_sdk_bedrock.types.automated_evaluation_config

        return {
            "automated": aws_sdk_bedrock.types.automated_evaluation_config.deserialize_json(
                data["automated"]
            )
        }
    elif "human" in data:
        import aws_sdk_bedrock.types.human_evaluation_config

        return {
            "human": aws_sdk_bedrock.types.human_evaluation_config.deserialize_json(
                data["human"]
            )
        }
    else:
        raise DeserializationError("EvaluationConfig: no recognized variant key")
