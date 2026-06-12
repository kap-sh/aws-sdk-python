"""Generated from Smithy shape ``com.amazonaws.mq#ChangeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mq.errors import DeserializationError

"""<p>The type of change pending for the ActiveMQ user.</p>"""
ChangeType: TypeAlias = Literal[
    "CREATE",
    "UPDATE",
    "DELETE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE",
        "UPDATE",
        "DELETE",
    )
)


def serialize_json(value: ChangeType) -> str:
    return value


def deserialize_json(data: str) -> ChangeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChangeType value: {data!r}")
    return cast(ChangeType, data)
