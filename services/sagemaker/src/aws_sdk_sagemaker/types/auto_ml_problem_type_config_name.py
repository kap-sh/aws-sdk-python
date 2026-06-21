"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLProblemTypeConfigName``."""

from typing import Literal, TypeAlias, cast

AutoMLProblemTypeConfigName: TypeAlias = Literal[
    "ImageClassification",
    "TextClassification",
    "TimeSeriesForecasting",
    "Tabular",
    "TextGeneration",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLProblemTypeConfigName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoMLProblemTypeConfigName:
    return cast(AutoMLProblemTypeConfigName, data)
