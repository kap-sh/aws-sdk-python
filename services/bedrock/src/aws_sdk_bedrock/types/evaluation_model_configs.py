"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationModelConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.evaluation_model_config

EvaluationModelConfigs: TypeAlias = list[
    "aws_sdk_bedrock.types.evaluation_model_config.EvaluationModelConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationModelConfigs) -> list:
    import aws_sdk_bedrock.types.evaluation_model_config

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock.types.evaluation_model_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> EvaluationModelConfigs:
    import aws_sdk_bedrock.types.evaluation_model_config

    out: EvaluationModelConfigs = []
    for item in data:
        out.append(aws_sdk_bedrock.types.evaluation_model_config.deserialize_json(item))
    return out
