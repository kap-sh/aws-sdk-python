"""Generated from Smithy shape ``com.amazonaws.applicationcostprofiler#ReportFrequency``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_applicationcostprofiler.errors import DeserializationError

ReportFrequency: TypeAlias = Literal[
    "MONTHLY",
    "DAILY",
    "ALL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MONTHLY",
        "DAILY",
        "ALL",
    )
)


def serialize_json(value: ReportFrequency) -> str:
    return value


def deserialize_json(data: str) -> ReportFrequency:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReportFrequency value: {data!r}")
    return cast(ReportFrequency, data)
