"""Generated from Smithy shape ``com.amazonaws.medialive#DashRoleAudio``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: DashRoleAudio) -> str:
    return value


def deserialize_json(data: str) -> DashRoleAudio:
    return cast(DashRoleAudio, data)
