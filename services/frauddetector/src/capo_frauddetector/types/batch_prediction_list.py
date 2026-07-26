"""Generated from Smithy shape ``com.amazonaws.frauddetector#BatchPredictionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.batch_prediction

BatchPredictionList: TypeAlias = list[
    "capo_frauddetector.types.batch_prediction.BatchPrediction"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchPredictionList) -> list:
    import capo_frauddetector.types.batch_prediction

    out: list = []
    for item in value:
        out.append(
            capo_frauddetector.types.batch_prediction.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchPredictionList:
    import capo_frauddetector.types.batch_prediction

    out: BatchPredictionList = []
    for item in data:
        out.append(
            capo_frauddetector.types.batch_prediction.deserialize_aws_json_1_1(item)
        )
    return out
