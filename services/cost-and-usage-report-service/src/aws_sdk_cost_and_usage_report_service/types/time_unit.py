"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#TimeUnit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_and_usage_report_service.errors import DeserializationError

"""<p>The length of time covered by the report. </p>"""
TimeUnit: TypeAlias = Literal[
    "HOURLY",
    "DAILY",
    "MONTHLY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HOURLY",
        "DAILY",
        "MONTHLY",
    )
)


def serialize_aws_json_1_1(value: TimeUnit) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TimeUnit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TimeUnit value: {data!r}")
    return cast(TimeUnit, data)
