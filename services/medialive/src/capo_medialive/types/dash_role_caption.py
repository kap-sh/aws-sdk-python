"""Generated from Smithy shape ``com.amazonaws.medialive#DashRoleCaption``."""

from typing import Literal, TypeAlias, cast

"""Dash Role Caption"""
DashRoleCaption: TypeAlias = Literal[
    "ALTERNATE",
    "CAPTION",
    "COMMENTARY",
    "DESCRIPTION",
    "DUB",
    "EASYREADER",
    "EMERGENCY",
    "FORCED-SUBTITLE",
    "KARAOKE",
    "MAIN",
    "METADATA",
    "SUBTITLE",
    "SUPPLEMENTARY",
]


# --- restJson1 ser/de ---
def serialize_json(value: DashRoleCaption) -> str:
    return value


def deserialize_json(data: str) -> DashRoleCaption:
    return cast(DashRoleCaption, data)
