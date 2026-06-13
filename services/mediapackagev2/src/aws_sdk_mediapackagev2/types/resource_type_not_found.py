"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ResourceTypeNotFound``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackagev2.errors import DeserializationError

ResourceTypeNotFound: TypeAlias = Literal[
    "CHANNEL_GROUP",
    "CHANNEL",
    "ORIGIN_ENDPOINT",
    "HARVEST_JOB",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CHANNEL_GROUP",
        "CHANNEL",
        "ORIGIN_ENDPOINT",
        "HARVEST_JOB",
    )
)


def serialize_json(value: ResourceTypeNotFound) -> str:
    return value


def deserialize_json(data: str) -> ResourceTypeNotFound:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceTypeNotFound value: {data!r}")
    return cast(ResourceTypeNotFound, data)
