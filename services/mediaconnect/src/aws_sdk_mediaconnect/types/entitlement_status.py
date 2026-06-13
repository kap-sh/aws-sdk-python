"""Generated from Smithy shape ``com.amazonaws.mediaconnect#EntitlementStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

EntitlementStatus: TypeAlias = Literal[
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


def serialize_json(value: EntitlementStatus) -> str:
    return value


def deserialize_json(data: str) -> EntitlementStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EntitlementStatus value: {data!r}")
    return cast(EntitlementStatus, data)
