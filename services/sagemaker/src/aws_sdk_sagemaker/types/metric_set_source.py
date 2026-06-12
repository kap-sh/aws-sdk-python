"""Generated from Smithy shape ``com.amazonaws.sagemaker#MetricSetSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

MetricSetSource: TypeAlias = Literal[
    "Train",
    "Validation",
    "Test",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Train",
        "Validation",
        "Test",
    )
)


def serialize_aws_json_1_1(value: MetricSetSource) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MetricSetSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MetricSetSource value: {data!r}")
    return cast(MetricSetSource, data)
