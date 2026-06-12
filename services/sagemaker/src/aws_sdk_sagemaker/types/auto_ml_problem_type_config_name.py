"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLProblemTypeConfigName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AutoMLProblemTypeConfigName: TypeAlias = Literal[
    "ImageClassification",
    "TextClassification",
    "TimeSeriesForecasting",
    "Tabular",
    "TextGeneration",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ImageClassification",
        "TextClassification",
        "TimeSeriesForecasting",
        "Tabular",
        "TextGeneration",
    )
)


def serialize_aws_json_1_1(value: AutoMLProblemTypeConfigName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoMLProblemTypeConfigName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AutoMLProblemTypeConfigName value: {data!r}"
        )
    return cast(AutoMLProblemTypeConfigName, data)
