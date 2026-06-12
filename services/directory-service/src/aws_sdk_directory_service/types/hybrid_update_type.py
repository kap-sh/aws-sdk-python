"""Generated from Smithy shape ``com.amazonaws.directoryservice#HybridUpdateType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

HybridUpdateType: TypeAlias = Literal[
    "SelfManagedInstances",
    "HybridAdministratorAccount",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SelfManagedInstances",
        "HybridAdministratorAccount",
    )
)


def serialize_aws_json_1_1(value: HybridUpdateType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HybridUpdateType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HybridUpdateType value: {data!r}")
    return cast(HybridUpdateType, data)
