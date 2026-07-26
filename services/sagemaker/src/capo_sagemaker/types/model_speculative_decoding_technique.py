"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelSpeculativeDecodingTechnique``."""

from typing import Literal, TypeAlias, cast

ModelSpeculativeDecodingTechnique: TypeAlias = Literal["EAGLE",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelSpeculativeDecodingTechnique) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelSpeculativeDecodingTechnique:
    return cast(ModelSpeculativeDecodingTechnique, data)
