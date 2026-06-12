"""Generated from Smithy shape ``com.amazonaws.iot#ReportType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

ReportType: TypeAlias = Literal[
    "ERRORS",
    "RESULTS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ERRORS",
        "RESULTS",
    )
)


def serialize_json(value: ReportType) -> str:
    return value


def deserialize_json(data: str) -> ReportType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReportType value: {data!r}")
    return cast(ReportType, data)
