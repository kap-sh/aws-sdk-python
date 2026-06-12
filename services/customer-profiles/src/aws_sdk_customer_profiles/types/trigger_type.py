"""Generated from Smithy shape ``com.amazonaws.customerprofiles#TriggerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

TriggerType: TypeAlias = Literal[
    "Scheduled",
    "Event",
    "OnDemand",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Scheduled",
        "Event",
        "OnDemand",
    )
)


def serialize_json(value: TriggerType) -> str:
    return value


def deserialize_json(data: str) -> TriggerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TriggerType value: {data!r}")
    return cast(TriggerType, data)
