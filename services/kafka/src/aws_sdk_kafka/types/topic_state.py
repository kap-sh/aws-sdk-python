"""Generated from Smithy shape ``com.amazonaws.kafka#TopicState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kafka.errors import DeserializationError

"""<p>The state of a topic request.</p>"""
TopicState: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "DELETING",
    "ACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "UPDATING",
        "DELETING",
        "ACTIVE",
    )
)


def serialize_json(value: TopicState) -> str:
    return value


def deserialize_json(data: str) -> TopicState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TopicState value: {data!r}")
    return cast(TopicState, data)
