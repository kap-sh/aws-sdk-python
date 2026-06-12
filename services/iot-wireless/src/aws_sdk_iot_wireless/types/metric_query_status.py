"""Generated from Smithy shape ``com.amazonaws.iotwireless#MetricQueryStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

MetricQueryStatus: TypeAlias = Literal[
    "Succeeded",
    "Failed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Succeeded",
        "Failed",
    )
)


def serialize_json(value: MetricQueryStatus) -> str:
    return value


def deserialize_json(data: str) -> MetricQueryStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MetricQueryStatus value: {data!r}")
    return cast(MetricQueryStatus, data)
