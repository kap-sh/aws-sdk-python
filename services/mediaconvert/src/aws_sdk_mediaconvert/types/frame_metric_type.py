"""Generated from Smithy shape ``com.amazonaws.mediaconvert#FrameMetricType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""* PSNR: Peak Signal-to-Noise Ratio * SSIM: Structural Similarity Index Measure * MS_SSIM: Multi-Scale Similarity Index Measure * PSNR_HVS: Peak Signal-to-Noise Ratio, Human Visual System * VMAF: Video Multi-Method Assessment Fusion * QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode. * SHOT_CHANGE: Shot Changes"""
FrameMetricType: TypeAlias = Literal[
    "PSNR",
    "SSIM",
    "MS_SSIM",
    "PSNR_HVS",
    "VMAF",
    "QVBR",
    "SHOT_CHANGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PSNR",
        "SSIM",
        "MS_SSIM",
        "PSNR_HVS",
        "VMAF",
        "QVBR",
        "SHOT_CHANGE",
    )
)


def serialize_json(value: FrameMetricType) -> str:
    return value


def deserialize_json(data: str) -> FrameMetricType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FrameMetricType value: {data!r}")
    return cast(FrameMetricType, data)
