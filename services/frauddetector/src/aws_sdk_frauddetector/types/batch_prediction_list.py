"""Generated from Smithy shape ``com.amazonaws.frauddetector#BatchPredictionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.batch_prediction

BatchPredictionList: TypeAlias = list[
    "aws_sdk_frauddetector.types.batch_prediction.BatchPrediction"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchPredictionList) -> list:
    import aws_sdk_frauddetector.types.batch_prediction

    out: list = []
    for item in value:
        out.append(
            aws_sdk_frauddetector.types.batch_prediction.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchPredictionList:
    import aws_sdk_frauddetector.types.batch_prediction

    out: BatchPredictionList = []
    for item in data:
        out.append(
            aws_sdk_frauddetector.types.batch_prediction.deserialize_aws_json_1_1(item)
        )
    return out
