"""Generated from Smithy shape ``com.amazonaws.pinpoint#DeliveryStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint.errors import DeserializationError

DeliveryStatus: TypeAlias = Literal[
    "SUCCESSFUL",
    "THROTTLED",
    "TEMPORARY_FAILURE",
    "PERMANENT_FAILURE",
    "UNKNOWN_FAILURE",
    "OPT_OUT",
    "DUPLICATE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCESSFUL",
        "THROTTLED",
        "TEMPORARY_FAILURE",
        "PERMANENT_FAILURE",
        "UNKNOWN_FAILURE",
        "OPT_OUT",
        "DUPLICATE",
    )
)


def serialize_json(value: DeliveryStatus) -> str:
    return value


def deserialize_json(data: str) -> DeliveryStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeliveryStatus value: {data!r}")
    return cast(DeliveryStatus, data)
