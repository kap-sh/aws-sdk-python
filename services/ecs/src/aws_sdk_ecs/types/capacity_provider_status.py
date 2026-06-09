"""Generated from Smithy shape ``com.amazonaws.ecs#CapacityProviderStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

CapacityProviderStatus: TypeAlias = Literal[
    "PROVISIONING",
    "ACTIVE",
    "DEPROVISIONING",
    "INACTIVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROVISIONING",
        "ACTIVE",
        "DEPROVISIONING",
        "INACTIVE",
    )
)


def serialize_aws_json_1_1(value: CapacityProviderStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CapacityProviderStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CapacityProviderStatus value: {data!r}")
    return cast(CapacityProviderStatus, data)
