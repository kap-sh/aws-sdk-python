"""Generated from Smithy shape ``com.amazonaws.forecast#ScalingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_forecast.errors import DeserializationError

ScalingType: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: ScalingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScalingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScalingType value: {data!r}")
    return cast(ScalingType, data)
