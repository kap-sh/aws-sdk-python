"""Generated from Smithy shape ``com.amazonaws.medialive#DvbSdtOutputSdt``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Dvb Sdt Output Sdt"""
DvbSdtOutputSdt: TypeAlias = Literal[
    "SDT_FOLLOW",
    "SDT_FOLLOW_IF_PRESENT",
    "SDT_MANUAL",
    "SDT_NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SDT_FOLLOW",
        "SDT_FOLLOW_IF_PRESENT",
        "SDT_MANUAL",
        "SDT_NONE",
    )
)


def serialize_json(value: DvbSdtOutputSdt) -> str:
    return value


def deserialize_json(data: str) -> DvbSdtOutputSdt:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DvbSdtOutputSdt value: {data!r}")
    return cast(DvbSdtOutputSdt, data)
