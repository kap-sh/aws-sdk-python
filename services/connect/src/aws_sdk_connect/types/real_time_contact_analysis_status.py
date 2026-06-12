"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

RealTimeContactAnalysisStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "FAILED",
    "COMPLETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "FAILED",
        "COMPLETED",
    )
)


def serialize_json(value: RealTimeContactAnalysisStatus) -> str:
    return value


def deserialize_json(data: str) -> RealTimeContactAnalysisStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RealTimeContactAnalysisStatus value: {data!r}"
        )
    return cast(RealTimeContactAnalysisStatus, data)
