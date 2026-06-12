"""Generated from Smithy shape ``com.amazonaws.devicefarm#SampleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_device_farm.errors import DeserializationError

SampleType: TypeAlias = Literal[
    "CPU",
    "MEMORY",
    "THREADS",
    "RX_RATE",
    "TX_RATE",
    "RX",
    "TX",
    "NATIVE_FRAMES",
    "NATIVE_FPS",
    "NATIVE_MIN_DRAWTIME",
    "NATIVE_AVG_DRAWTIME",
    "NATIVE_MAX_DRAWTIME",
    "OPENGL_FRAMES",
    "OPENGL_FPS",
    "OPENGL_MIN_DRAWTIME",
    "OPENGL_AVG_DRAWTIME",
    "OPENGL_MAX_DRAWTIME",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CPU",
        "MEMORY",
        "THREADS",
        "RX_RATE",
        "TX_RATE",
        "RX",
        "TX",
        "NATIVE_FRAMES",
        "NATIVE_FPS",
        "NATIVE_MIN_DRAWTIME",
        "NATIVE_AVG_DRAWTIME",
        "NATIVE_MAX_DRAWTIME",
        "OPENGL_FRAMES",
        "OPENGL_FPS",
        "OPENGL_MIN_DRAWTIME",
        "OPENGL_AVG_DRAWTIME",
        "OPENGL_MAX_DRAWTIME",
    )
)


def serialize_aws_json_1_1(value: SampleType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SampleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SampleType value: {data!r}")
    return cast(SampleType, data)
