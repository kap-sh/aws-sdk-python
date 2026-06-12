"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringProblemType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

MonitoringProblemType: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: MonitoringProblemType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MonitoringProblemType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MonitoringProblemType value: {data!r}")
    return cast(MonitoringProblemType, data)
