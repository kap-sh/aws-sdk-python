"""Generated from Smithy shape ``com.amazonaws.kinesisvideosignaling#Service``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_video_signaling.errors import DeserializationError

Service: TypeAlias = Literal["TURN",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TURN",))


def serialize_json(value: Service) -> str:
    return value


def deserialize_json(data: str) -> Service:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Service value: {data!r}")
    return cast(Service, data)
