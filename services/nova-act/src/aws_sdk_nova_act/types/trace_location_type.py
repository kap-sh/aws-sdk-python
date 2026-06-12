"""Generated from Smithy shape ``com.amazonaws.novaact#TraceLocationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_nova_act.errors import DeserializationError

TraceLocationType: TypeAlias = Literal["S3",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("S3",))


def serialize_json(value: TraceLocationType) -> str:
    return value


def deserialize_json(data: str) -> TraceLocationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TraceLocationType value: {data!r}")
    return cast(TraceLocationType, data)
