"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterScalingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

HyperParameterScalingType: TypeAlias = Literal[
    "Auto",
    "Linear",
    "Logarithmic",
    "ReverseLogarithmic",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Auto",
        "Linear",
        "Logarithmic",
        "ReverseLogarithmic",
    )
)


def serialize_aws_json_1_1(value: HyperParameterScalingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HyperParameterScalingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HyperParameterScalingType value: {data!r}")
    return cast(HyperParameterScalingType, data)
