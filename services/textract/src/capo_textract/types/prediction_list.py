"""Generated from Smithy shape ``com.amazonaws.textract#PredictionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.prediction

PredictionList: TypeAlias = list["capo_textract.types.prediction.Prediction"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictionList) -> list:
    import capo_textract.types.prediction

    out: list = []
    for item in value:
        out.append(capo_textract.types.prediction.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PredictionList:
    import capo_textract.types.prediction

    out: PredictionList = []
    for item in data:
        out.append(capo_textract.types.prediction.deserialize_aws_json_1_1(item))
    return out
