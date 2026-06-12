"""Generated from Smithy shape ``com.amazonaws.medialive#DashRoleAudio``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Dash Role Audio"""
DashRoleAudio: TypeAlias = Literal[
    "ALTERNATE",
    "COMMENTARY",
    "DESCRIPTION",
    "DUB",
    "EMERGENCY",
    "ENHANCED-AUDIO-INTELLIGIBILITY",
    "KARAOKE",
    "MAIN",
    "SUPPLEMENTARY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALTERNATE",
        "COMMENTARY",
        "DESCRIPTION",
        "DUB",
        "EMERGENCY",
        "ENHANCED-AUDIO-INTELLIGIBILITY",
        "KARAOKE",
        "MAIN",
        "SUPPLEMENTARY",
    )
)


def serialize_json(value: DashRoleAudio) -> str:
    return value


def deserialize_json(data: str) -> DashRoleAudio:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DashRoleAudio value: {data!r}")
    return cast(DashRoleAudio, data)
