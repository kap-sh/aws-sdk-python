"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H264ScanTypeConversionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Use this setting for interlaced outputs, when your output frame rate is half of your input frame rate. In this situation, choose Optimized interlacing to create a better quality interlaced output. In this case, each progressive frame from the input corresponds to an interlaced field in the output. Keep the default value, Basic interlacing, for all other output frame rates. With basic interlacing, MediaConvert performs any frame rate conversion first and then interlaces the frames. When you choose Optimized interlacing and you set your output frame rate to a value that isn't suitable for optimized interlacing, MediaConvert automatically falls back to basic interlacing. Required settings: To use optimized interlacing, you must set Telecine to None or Soft. You can't use optimized interlacing for hard telecine outputs. You must also set Interlace mode to a value other than Progressive."""
H264ScanTypeConversionMode: TypeAlias = Literal[
    "INTERLACED",
    "INTERLACED_OPTIMIZE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INTERLACED",
        "INTERLACED_OPTIMIZE",
    )
)


def serialize_json(value: H264ScanTypeConversionMode) -> str:
    return value


def deserialize_json(data: str) -> H264ScanTypeConversionMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown H264ScanTypeConversionMode value: {data!r}"
        )
    return cast(H264ScanTypeConversionMode, data)
