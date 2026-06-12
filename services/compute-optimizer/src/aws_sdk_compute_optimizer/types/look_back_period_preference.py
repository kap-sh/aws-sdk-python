"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LookBackPeriodPreference``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

LookBackPeriodPreference: TypeAlias = Literal[
    "DAYS_14",
    "DAYS_32",
    "DAYS_93",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DAYS_14",
        "DAYS_32",
        "DAYS_93",
    )
)


def serialize_aws_json_1_0(value: LookBackPeriodPreference) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LookBackPeriodPreference:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LookBackPeriodPreference value: {data!r}")
    return cast(LookBackPeriodPreference, data)
