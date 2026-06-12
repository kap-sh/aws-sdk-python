"""Generated from Smithy shape ``com.amazonaws.medialive#ChannelClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""A standard channel has two encoding pipelines and a single pipeline channel only has one."""
ChannelClass: TypeAlias = Literal[
    "STANDARD",
    "SINGLE_PIPELINE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "SINGLE_PIPELINE",
    )
)


def serialize_json(value: ChannelClass) -> str:
    return value


def deserialize_json(data: str) -> ChannelClass:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChannelClass value: {data!r}")
    return cast(ChannelClass, data)
