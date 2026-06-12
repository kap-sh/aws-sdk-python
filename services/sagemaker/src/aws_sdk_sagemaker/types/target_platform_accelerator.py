"""Generated from Smithy shape ``com.amazonaws.sagemaker#TargetPlatformAccelerator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

TargetPlatformAccelerator: TypeAlias = Literal[
    "INTEL_GRAPHICS",
    "MALI",
    "NVIDIA",
    "NNA",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INTEL_GRAPHICS",
        "MALI",
        "NVIDIA",
        "NNA",
    )
)


def serialize_aws_json_1_1(value: TargetPlatformAccelerator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TargetPlatformAccelerator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetPlatformAccelerator value: {data!r}")
    return cast(TargetPlatformAccelerator, data)
