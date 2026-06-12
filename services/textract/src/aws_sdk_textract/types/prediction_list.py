"""Generated from Smithy shape ``com.amazonaws.textract#PredictionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_textract.types.prediction

PredictionList: TypeAlias = list["aws_sdk_textract.types.prediction.Prediction"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictionList) -> list:
    import aws_sdk_textract.types.prediction

    out: list = []
    for item in value:
        out.append(aws_sdk_textract.types.prediction.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PredictionList:
    import aws_sdk_textract.types.prediction

    out: PredictionList = []
    for item in data:
        out.append(aws_sdk_textract.types.prediction.deserialize_aws_json_1_1(item))
    return out
