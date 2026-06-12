"""Generated from Smithy shape ``com.amazonaws.connect#InitiateAs``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

InitiateAs: TypeAlias = Literal[
    "CONNECTED_TO_USER",
    "COMPLETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONNECTED_TO_USER",
        "COMPLETED",
    )
)


def serialize_json(value: InitiateAs) -> str:
    return value


def deserialize_json(data: str) -> InitiateAs:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InitiateAs value: {data!r}")
    return cast(InitiateAs, data)
