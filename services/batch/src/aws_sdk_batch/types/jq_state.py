"""Generated from Smithy shape ``com.amazonaws.batch#JQState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

JQState: TypeAlias = Literal[
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


def serialize_json(value: JQState) -> str:
    return value


def deserialize_json(data: str) -> JQState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JQState value: {data!r}")
    return cast(JQState, data)
