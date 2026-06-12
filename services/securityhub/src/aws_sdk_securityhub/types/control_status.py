"""Generated from Smithy shape ``com.amazonaws.securityhub#ControlStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

ControlStatus: TypeAlias = Literal[
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


def serialize_json(value: ControlStatus) -> str:
    return value


def deserialize_json(data: str) -> ControlStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ControlStatus value: {data!r}")
    return cast(ControlStatus, data)
