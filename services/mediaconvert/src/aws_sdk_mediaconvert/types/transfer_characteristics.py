"""Generated from Smithy shape ``com.amazonaws.mediaconvert#TransferCharacteristics``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""The color space transfer characteristics of the video track, defining the relationship between linear light values and the encoded signal values. This affects brightness and contrast reproduction."""
TransferCharacteristics: TypeAlias = Literal[
    "ITU_709",
    "UNSPECIFIED",
    "RESERVED",
    "ITU_470M",
    "ITU_470BG",
    "SMPTE_170M",
    "SMPTE_240M",
    "LINEAR",
    "LOG10_2",
    "LOC10_2_5",
    "IEC_61966_2_4",
    "ITU_1361",
    "IEC_61966_2_1",
    "ITU_2020_10bit",
    "ITU_2020_12bit",
    "SMPTE_2084",
    "SMPTE_428_1",
    "ARIB_B67",
    "LAST",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ITU_709",
        "UNSPECIFIED",
        "RESERVED",
        "ITU_470M",
        "ITU_470BG",
        "SMPTE_170M",
        "SMPTE_240M",
        "LINEAR",
        "LOG10_2",
        "LOC10_2_5",
        "IEC_61966_2_4",
        "ITU_1361",
        "IEC_61966_2_1",
        "ITU_2020_10bit",
        "ITU_2020_12bit",
        "SMPTE_2084",
        "SMPTE_428_1",
        "ARIB_B67",
        "LAST",
    )
)


def serialize_json(value: TransferCharacteristics) -> str:
    return value


def deserialize_json(data: str) -> TransferCharacteristics:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TransferCharacteristics value: {data!r}")
    return cast(TransferCharacteristics, data)
