"""Generated from Smithy shape ``com.amazonaws.iotwireless#SummaryMetricConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

SummaryMetricConfigurationStatus: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enabled",
        "Disabled",
    )
)


def serialize_json(value: SummaryMetricConfigurationStatus) -> str:
    return value


def deserialize_json(data: str) -> SummaryMetricConfigurationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SummaryMetricConfigurationStatus value: {data!r}"
        )
    return cast(SummaryMetricConfigurationStatus, data)
