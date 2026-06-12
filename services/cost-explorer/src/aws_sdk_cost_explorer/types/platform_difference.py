"""Generated from Smithy shape ``com.amazonaws.costexplorer#PlatformDifference``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

PlatformDifference: TypeAlias = Literal[
    "HYPERVISOR",
    "NETWORK_INTERFACE",
    "STORAGE_INTERFACE",
    "INSTANCE_STORE_AVAILABILITY",
    "VIRTUALIZATION_TYPE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HYPERVISOR",
        "NETWORK_INTERFACE",
        "STORAGE_INTERFACE",
        "INSTANCE_STORE_AVAILABILITY",
        "VIRTUALIZATION_TYPE",
    )
)


def serialize_aws_json_1_1(value: PlatformDifference) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PlatformDifference:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PlatformDifference value: {data!r}")
    return cast(PlatformDifference, data)
