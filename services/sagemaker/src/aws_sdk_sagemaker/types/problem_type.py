"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProblemType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ProblemType: TypeAlias = Literal[
    "BinaryClassification",
    "MulticlassClassification",
    "Regression",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BinaryClassification",
        "MulticlassClassification",
        "Regression",
    )
)


def serialize_aws_json_1_1(value: ProblemType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProblemType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProblemType value: {data!r}")
    return cast(ProblemType, data)
