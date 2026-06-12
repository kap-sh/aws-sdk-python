"""Generated from Smithy shape ``com.amazonaws.budgets#HealthStatusValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_budgets.errors import DeserializationError

HealthStatusValue: TypeAlias = Literal[
    "HEALTHY",
    "UNHEALTHY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HEALTHY",
        "UNHEALTHY",
    )
)


def serialize_aws_json_1_1(value: HealthStatusValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HealthStatusValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HealthStatusValue value: {data!r}")
    return cast(HealthStatusValue, data)
