"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#LiveConnectorSinkType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

LiveConnectorSinkType: TypeAlias = Literal["RTMP",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("RTMP",))


def serialize_json(value: LiveConnectorSinkType) -> str:
    return value


def deserialize_json(data: str) -> LiveConnectorSinkType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LiveConnectorSinkType value: {data!r}")
    return cast(LiveConnectorSinkType, data)
