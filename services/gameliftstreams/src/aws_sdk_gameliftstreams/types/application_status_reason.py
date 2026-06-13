"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#ApplicationStatusReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gameliftstreams.errors import DeserializationError

ApplicationStatusReason: TypeAlias = Literal[
    "internalError",
    "accessDenied",
    "sourceModified",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "internalError",
        "accessDenied",
        "sourceModified",
    )
)


def serialize_json(value: ApplicationStatusReason) -> str:
    return value


def deserialize_json(data: str) -> ApplicationStatusReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApplicationStatusReason value: {data!r}")
    return cast(ApplicationStatusReason, data)
