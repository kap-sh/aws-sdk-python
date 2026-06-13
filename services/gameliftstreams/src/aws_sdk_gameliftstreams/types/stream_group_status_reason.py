"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#StreamGroupStatusReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gameliftstreams.errors import DeserializationError

StreamGroupStatusReason: TypeAlias = Literal[
    "internalError",
    "noAvailableInstances",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "internalError",
        "noAvailableInstances",
    )
)


def serialize_json(value: StreamGroupStatusReason) -> str:
    return value


def deserialize_json(data: str) -> StreamGroupStatusReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StreamGroupStatusReason value: {data!r}")
    return cast(StreamGroupStatusReason, data)
