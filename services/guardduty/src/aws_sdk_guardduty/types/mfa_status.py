"""Generated from Smithy shape ``com.amazonaws.guardduty#MfaStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

MfaStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: MfaStatus) -> str:
    return value


def deserialize_json(data: str) -> MfaStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MfaStatus value: {data!r}")
    return cast(MfaStatus, data)
