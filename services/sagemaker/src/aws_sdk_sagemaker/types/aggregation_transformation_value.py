"""Generated from Smithy shape ``com.amazonaws.sagemaker#AggregationTransformationValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AggregationTransformationValue: TypeAlias = Literal[
    "sum",
    "avg",
    "first",
    "min",
    "max",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "sum",
        "avg",
        "first",
        "min",
        "max",
    )
)


def serialize_aws_json_1_1(value: AggregationTransformationValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AggregationTransformationValue:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AggregationTransformationValue value: {data!r}"
        )
    return cast(AggregationTransformationValue, data)
