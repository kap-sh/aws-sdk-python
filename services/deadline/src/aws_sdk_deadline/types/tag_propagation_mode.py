"""Generated from Smithy shape ``com.amazonaws.deadline#TagPropagationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

TagPropagationMode: TypeAlias = Literal[
    "NO_PROPAGATION",
    "PROPAGATE_TAGS_TO_WORKERS_AT_LAUNCH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_PROPAGATION",
        "PROPAGATE_TAGS_TO_WORKERS_AT_LAUNCH",
    )
)


def serialize_json(value: TagPropagationMode) -> str:
    return value


def deserialize_json(data: str) -> TagPropagationMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TagPropagationMode value: {data!r}")
    return cast(TagPropagationMode, data)
