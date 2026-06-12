"""Generated from Smithy shape ``com.amazonaws.sagemaker#Statistic``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

Statistic: TypeAlias = Literal[
    "Average",
    "Minimum",
    "Maximum",
    "SampleCount",
    "Sum",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Average",
        "Minimum",
        "Maximum",
        "SampleCount",
        "Sum",
    )
)


def serialize_aws_json_1_1(value: Statistic) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Statistic:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Statistic value: {data!r}")
    return cast(Statistic, data)
