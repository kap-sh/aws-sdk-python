"""Generated from Smithy shape ``com.amazonaws.medialive#DashRoleCaption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: DashRoleCaption) -> str:
    return value


def deserialize_json(data: str) -> DashRoleCaption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DashRoleCaption value: {data!r}")
    return cast(DashRoleCaption, data)
