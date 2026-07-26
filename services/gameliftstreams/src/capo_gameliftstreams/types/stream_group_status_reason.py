"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#StreamGroupStatusReason``."""

from typing import Literal, TypeAlias, cast

StreamGroupStatusReason: TypeAlias = Literal[
    "internalError",
    "noAvailableInstances",
]


# --- restJson1 ser/de ---
def serialize_json(value: StreamGroupStatusReason) -> str:
    return value


def deserialize_json(data: str) -> StreamGroupStatusReason:
    return cast(StreamGroupStatusReason, data)
