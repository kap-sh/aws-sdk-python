"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DashIsoHbbtvCompliance``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Supports HbbTV specification as indicated"""
DashIsoHbbtvCompliance: TypeAlias = Literal[
    "HBBTV_1_5",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HBBTV_1_5",
        "NONE",
    )
)


def serialize_json(value: DashIsoHbbtvCompliance) -> str:
    return value


def deserialize_json(data: str) -> DashIsoHbbtvCompliance:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DashIsoHbbtvCompliance value: {data!r}")
    return cast(DashIsoHbbtvCompliance, data)
