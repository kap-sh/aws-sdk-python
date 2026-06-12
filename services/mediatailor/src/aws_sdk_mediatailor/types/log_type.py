"""Generated from Smithy shape ``com.amazonaws.mediatailor#LogType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediatailor.errors import DeserializationError

LogType: TypeAlias = Literal["AS_RUN",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("AS_RUN",))


def serialize_json(value: LogType) -> str:
    return value


def deserialize_json(data: str) -> LogType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogType value: {data!r}")
    return cast(LogType, data)
