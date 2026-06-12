"""Generated from Smithy shape ``com.amazonaws.servicequotas#PeriodUnit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_quotas.errors import DeserializationError

PeriodUnit: TypeAlias = Literal[
    "MICROSECOND",
    "MILLISECOND",
    "SECOND",
    "MINUTE",
    "HOUR",
    "DAY",
    "WEEK",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MICROSECOND",
        "MILLISECOND",
        "SECOND",
        "MINUTE",
        "HOUR",
        "DAY",
        "WEEK",
    )
)


def serialize_aws_json_1_1(value: PeriodUnit) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PeriodUnit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PeriodUnit value: {data!r}")
    return cast(PeriodUnit, data)
