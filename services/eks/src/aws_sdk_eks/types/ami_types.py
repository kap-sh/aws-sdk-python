"""Generated from Smithy shape ``com.amazonaws.eks#AMITypes``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eks.errors import DeserializationError

AMITypes: TypeAlias = Literal[
    "AL2_x86_64",
    "AL2_x86_64_GPU",
    "AL2_ARM_64",
    "CUSTOM",
    "BOTTLEROCKET_ARM_64",
    "BOTTLEROCKET_x86_64",
    "BOTTLEROCKET_ARM_64_FIPS",
    "BOTTLEROCKET_x86_64_FIPS",
    "BOTTLEROCKET_ARM_64_NVIDIA",
    "BOTTLEROCKET_x86_64_NVIDIA",
    "BOTTLEROCKET_ARM_64_NVIDIA_FIPS",
    "BOTTLEROCKET_x86_64_NVIDIA_FIPS",
    "WINDOWS_CORE_2019_x86_64",
    "WINDOWS_FULL_2019_x86_64",
    "WINDOWS_CORE_2022_x86_64",
    "WINDOWS_FULL_2022_x86_64",
    "WINDOWS_CORE_2025_x86_64",
    "WINDOWS_FULL_2025_x86_64",
    "AL2023_x86_64_STANDARD",
    "AL2023_ARM_64_STANDARD",
    "AL2023_x86_64_NEURON",
    "AL2023_x86_64_NVIDIA",
    "AL2023_ARM_64_NVIDIA",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AL2_x86_64",
        "AL2_x86_64_GPU",
        "AL2_ARM_64",
        "CUSTOM",
        "BOTTLEROCKET_ARM_64",
        "BOTTLEROCKET_x86_64",
        "BOTTLEROCKET_ARM_64_FIPS",
        "BOTTLEROCKET_x86_64_FIPS",
        "BOTTLEROCKET_ARM_64_NVIDIA",
        "BOTTLEROCKET_x86_64_NVIDIA",
        "BOTTLEROCKET_ARM_64_NVIDIA_FIPS",
        "BOTTLEROCKET_x86_64_NVIDIA_FIPS",
        "WINDOWS_CORE_2019_x86_64",
        "WINDOWS_FULL_2019_x86_64",
        "WINDOWS_CORE_2022_x86_64",
        "WINDOWS_FULL_2022_x86_64",
        "WINDOWS_CORE_2025_x86_64",
        "WINDOWS_FULL_2025_x86_64",
        "AL2023_x86_64_STANDARD",
        "AL2023_ARM_64_STANDARD",
        "AL2023_x86_64_NEURON",
        "AL2023_x86_64_NVIDIA",
        "AL2023_ARM_64_NVIDIA",
    )
)


def serialize_json(value: AMITypes) -> str:
    return value


def deserialize_json(data: str) -> AMITypes:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AMITypes value: {data!r}")
    return cast(AMITypes, data)
