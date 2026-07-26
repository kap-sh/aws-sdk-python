"""Generated from Smithy shape ``com.amazonaws.bedrock#GraderConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock.types.lambda_grader_config


class _GraderConfig_lambdaGrader(TypedDict, closed=True):
    lambdaGrader: "capo_bedrock.types.lambda_grader_config.LambdaGraderConfig"


GraderConfig: TypeAlias = _GraderConfig_lambdaGrader


# --- restJson1 ser/de ---
def serialize_json(value: GraderConfig) -> dict:
    if "lambdaGrader" in value:
        import capo_bedrock.types.lambda_grader_config

        return {
            "lambdaGrader": capo_bedrock.types.lambda_grader_config.serialize_json(
                value["lambdaGrader"]
            )
        }
    else:
        raise SerializationError("GraderConfig: no variant present")


def deserialize_json(data: dict) -> GraderConfig:
    if "lambdaGrader" in data:
        import capo_bedrock.types.lambda_grader_config

        return {
            "lambdaGrader": capo_bedrock.types.lambda_grader_config.deserialize_json(
                data["lambdaGrader"]
            )
        }
    else:
        raise DeserializationError("GraderConfig: no recognized variant key")
