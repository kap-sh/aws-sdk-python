"""Generated from Smithy shape ``com.amazonaws.deadline#RunAs``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

RunAs: TypeAlias = Literal[
    "QUEUE_CONFIGURED_USER",
    "WORKER_AGENT_USER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUEUE_CONFIGURED_USER",
        "WORKER_AGENT_USER",
    )
)


def serialize_json(value: RunAs) -> str:
    return value


def deserialize_json(data: str) -> RunAs:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RunAs value: {data!r}")
    return cast(RunAs, data)
