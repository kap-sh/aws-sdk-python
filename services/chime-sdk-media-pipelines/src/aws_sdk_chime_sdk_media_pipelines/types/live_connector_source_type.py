"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#LiveConnectorSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

LiveConnectorSourceType: TypeAlias = Literal["ChimeSdkMeeting",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ChimeSdkMeeting",))


def serialize_json(value: LiveConnectorSourceType) -> str:
    return value


def deserialize_json(data: str) -> LiveConnectorSourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LiveConnectorSourceType value: {data!r}")
    return cast(LiveConnectorSourceType, data)
