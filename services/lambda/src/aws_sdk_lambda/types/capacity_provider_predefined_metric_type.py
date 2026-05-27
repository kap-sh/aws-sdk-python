"""Generated from Smithy shape ``com.amazonaws.lambda#CapacityProviderPredefinedMetricType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_lambda.errors import DeserializationError

CapacityProviderPredefinedMetricType: TypeAlias = Literal[
    "LambdaCapacityProviderAverageCPUUtilization",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("LambdaCapacityProviderAverageCPUUtilization",))


def serialize_json(value: CapacityProviderPredefinedMetricType) -> str:
    return value


def deserialize_json(data: str) -> CapacityProviderPredefinedMetricType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CapacityProviderPredefinedMetricType value: {data!r}"
        )
    return cast(CapacityProviderPredefinedMetricType, data)
