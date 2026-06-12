"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisOutputType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

RealTimeContactAnalysisOutputType: TypeAlias = Literal[
    "Raw",
    "Redacted",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Raw",
        "Redacted",
    )
)


def serialize_json(value: RealTimeContactAnalysisOutputType) -> str:
    return value


def deserialize_json(data: str) -> RealTimeContactAnalysisOutputType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RealTimeContactAnalysisOutputType value: {data!r}"
        )
    return cast(RealTimeContactAnalysisOutputType, data)
