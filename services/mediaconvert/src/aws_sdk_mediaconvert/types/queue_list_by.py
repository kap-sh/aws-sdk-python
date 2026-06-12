"""Generated from Smithy shape ``com.amazonaws.mediaconvert#QueueListBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Optional. When you request a list of queues, you can choose to list them alphabetically by NAME or chronologically by CREATION_DATE. If you don't specify, the service will list them by creation date."""
QueueListBy: TypeAlias = Literal[
    "NAME",
    "CREATION_DATE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NAME",
        "CREATION_DATE",
    )
)


def serialize_json(value: QueueListBy) -> str:
    return value


def deserialize_json(data: str) -> QueueListBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueueListBy value: {data!r}")
    return cast(QueueListBy, data)
