"""Generated from Smithy shape ``com.amazonaws.guardduty#PublicAccessStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

PublicAccessStatus: TypeAlias = Literal[
    "BLOCKED",
    "ALLOWED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BLOCKED",
        "ALLOWED",
    )
)


def serialize_json(value: PublicAccessStatus) -> str:
    return value


def deserialize_json(data: str) -> PublicAccessStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PublicAccessStatus value: {data!r}")
    return cast(PublicAccessStatus, data)
