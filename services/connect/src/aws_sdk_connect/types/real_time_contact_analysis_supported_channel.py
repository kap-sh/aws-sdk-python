"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisSupportedChannel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

RealTimeContactAnalysisSupportedChannel: TypeAlias = Literal[
    "VOICE",
    "CHAT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VOICE",
        "CHAT",
    )
)


def serialize_json(value: RealTimeContactAnalysisSupportedChannel) -> str:
    return value


def deserialize_json(data: str) -> RealTimeContactAnalysisSupportedChannel:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RealTimeContactAnalysisSupportedChannel value: {data!r}"
        )
    return cast(RealTimeContactAnalysisSupportedChannel, data)
