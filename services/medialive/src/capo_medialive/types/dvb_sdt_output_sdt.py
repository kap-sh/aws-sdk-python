"""Generated from Smithy shape ``com.amazonaws.medialive#DvbSdtOutputSdt``."""

from typing import Literal, TypeAlias, cast

"""Dvb Sdt Output Sdt"""
DvbSdtOutputSdt: TypeAlias = Literal[
    "SDT_FOLLOW",
    "SDT_FOLLOW_IF_PRESENT",
    "SDT_MANUAL",
    "SDT_NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DvbSdtOutputSdt) -> str:
    return value


def deserialize_json(data: str) -> DvbSdtOutputSdt:
    return cast(DvbSdtOutputSdt, data)
