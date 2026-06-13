"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ReportType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehubv2.errors import DeserializationError

ReportType: TypeAlias = Literal["FAILURE_MODE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("FAILURE_MODE",))


def serialize_json(value: ReportType) -> str:
    return value


def deserialize_json(data: str) -> ReportType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReportType value: {data!r}")
    return cast(ReportType, data)
