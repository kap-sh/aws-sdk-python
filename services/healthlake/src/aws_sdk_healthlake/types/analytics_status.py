"""Generated from Smithy shape ``com.amazonaws.healthlake#AnalyticsStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_healthlake.errors import DeserializationError

AnalyticsStatus: TypeAlias = Literal[
    "ENABLED",
    "ENABLING",
    "DISABLED",
    "DISABLING",
    "PAUSING",
    "PAUSED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "ENABLING",
        "DISABLED",
        "DISABLING",
        "PAUSING",
        "PAUSED",
    )
)


def serialize_aws_json_1_0(value: AnalyticsStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AnalyticsStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnalyticsStatus value: {data!r}")
    return cast(AnalyticsStatus, data)
