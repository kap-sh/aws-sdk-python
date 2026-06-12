"""Generated from Smithy shape ``com.amazonaws.connect#IvrRecordingTrack``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

IvrRecordingTrack: TypeAlias = Literal["ALL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ALL",))


def serialize_json(value: IvrRecordingTrack) -> str:
    return value


def deserialize_json(data: str) -> IvrRecordingTrack:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IvrRecordingTrack value: {data!r}")
    return cast(IvrRecordingTrack, data)
