"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#Status``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_serverlessapplicationrepository.errors import DeserializationError

Status: TypeAlias = Literal[
    "PREPARING",
    "ACTIVE",
    "EXPIRED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PREPARING",
        "ACTIVE",
        "EXPIRED",
    )
)


def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Status value: {data!r}")
    return cast(Status, data)
