"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ResourceTypeNotFound``."""

from typing import Literal, TypeAlias, cast

ResourceTypeNotFound: TypeAlias = Literal[
    "CHANNEL_GROUP",
    "CHANNEL",
    "ORIGIN_ENDPOINT",
    "HARVEST_JOB",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTypeNotFound) -> str:
    return value


def deserialize_json(data: str) -> ResourceTypeNotFound:
    return cast(ResourceTypeNotFound, data)
