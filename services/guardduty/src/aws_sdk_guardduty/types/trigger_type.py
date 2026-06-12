"""Generated from Smithy shape ``com.amazonaws.guardduty#TriggerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

TriggerType: TypeAlias = Literal[
    "BACKUP",
    "GUARDDUTY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BACKUP",
        "GUARDDUTY",
    )
)


def serialize_json(value: TriggerType) -> str:
    return value


def deserialize_json(data: str) -> TriggerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TriggerType value: {data!r}")
    return cast(TriggerType, data)
