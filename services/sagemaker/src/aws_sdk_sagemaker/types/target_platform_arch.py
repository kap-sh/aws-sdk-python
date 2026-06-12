"""Generated from Smithy shape ``com.amazonaws.sagemaker#TargetPlatformArch``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

TargetPlatformArch: TypeAlias = Literal[
    "X86_64",
    "X86",
    "ARM64",
    "ARM_EABI",
    "ARM_EABIHF",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "X86_64",
        "X86",
        "ARM64",
        "ARM_EABI",
        "ARM_EABIHF",
    )
)


def serialize_aws_json_1_1(value: TargetPlatformArch) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TargetPlatformArch:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetPlatformArch value: {data!r}")
    return cast(TargetPlatformArch, data)
