"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#PlatformDifference``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

PlatformDifference: TypeAlias = Literal[
    "Hypervisor",
    "NetworkInterface",
    "StorageInterface",
    "InstanceStoreAvailability",
    "VirtualizationType",
    "Architecture",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Hypervisor",
        "NetworkInterface",
        "StorageInterface",
        "InstanceStoreAvailability",
        "VirtualizationType",
        "Architecture",
    )
)


def serialize_aws_json_1_0(value: PlatformDifference) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PlatformDifference:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PlatformDifference value: {data!r}")
    return cast(PlatformDifference, data)
