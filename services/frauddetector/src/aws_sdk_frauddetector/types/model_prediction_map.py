"""Generated from Smithy shape ``com.amazonaws.frauddetector#ModelPredictionMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.float
    import aws_sdk_frauddetector.types.string

ModelPredictionMap: TypeAlias = dict[
    "aws_sdk_frauddetector.types.string.string",
    "aws_sdk_frauddetector.types.float.float",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ModelPredictionMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelPredictionMap:
    out: ModelPredictionMap = {}
    for key, value in data.items():
        out[key] = value
    return out
