"""Generated from Smithy shape ``com.amazonaws.securityhub#UpdateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

UpdateStatus: TypeAlias = Literal[
    "READY",
    "UPDATING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READY",
        "UPDATING",
    )
)


def serialize_json(value: UpdateStatus) -> str:
    return value


def deserialize_json(data: str) -> UpdateStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UpdateStatus value: {data!r}")
    return cast(UpdateStatus, data)
