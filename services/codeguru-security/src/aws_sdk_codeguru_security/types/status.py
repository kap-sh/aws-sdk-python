"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#Status``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeguru_security.errors import DeserializationError

Status: TypeAlias = Literal[
    "Closed",
    "Open",
    "All",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Closed",
        "Open",
        "All",
    )
)


def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Status value: {data!r}")
    return cast(Status, data)
