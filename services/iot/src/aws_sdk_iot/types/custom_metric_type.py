"""Generated from Smithy shape ``com.amazonaws.iot#CustomMetricType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

CustomMetricType: TypeAlias = Literal[
    "string-list",
    "ip-address-list",
    "number-list",
    "number",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "string-list",
        "ip-address-list",
        "number-list",
        "number",
    )
)


def serialize_json(value: CustomMetricType) -> str:
    return value


def deserialize_json(data: str) -> CustomMetricType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CustomMetricType value: {data!r}")
    return cast(CustomMetricType, data)
