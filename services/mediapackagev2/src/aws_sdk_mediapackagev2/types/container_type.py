"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ContainerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackagev2.errors import DeserializationError

ContainerType: TypeAlias = Literal[
    "TS",
    "CMAF",
    "ISM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TS",
        "CMAF",
        "ISM",
    )
)


def serialize_json(value: ContainerType) -> str:
    return value


def deserialize_json(data: str) -> ContainerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContainerType value: {data!r}")
    return cast(ContainerType, data)
