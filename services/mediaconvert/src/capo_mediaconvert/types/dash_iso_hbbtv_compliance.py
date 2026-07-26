"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DashIsoHbbtvCompliance``."""

from typing import Literal, TypeAlias, cast

"""Supports HbbTV specification as indicated"""
DashIsoHbbtvCompliance: TypeAlias = Literal[
    "HBBTV_1_5",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DashIsoHbbtvCompliance) -> str:
    return value


def deserialize_json(data: str) -> DashIsoHbbtvCompliance:
    return cast(DashIsoHbbtvCompliance, data)
