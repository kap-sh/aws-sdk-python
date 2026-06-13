"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ProvisionStateEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_instances.errors import DeserializationError

ProvisionStateEnum: TypeAlias = Literal[
    "ALLOCATING",
    "ALLOCATED",
    "DEALLOCATING",
    "DEALLOCATED",
    "ERROR_ALLOCATING",
    "ERROR_DEALLOCATING",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOCATING",
        "ALLOCATED",
        "DEALLOCATING",
        "DEALLOCATED",
        "ERROR_ALLOCATING",
        "ERROR_DEALLOCATING",
    )
)


def serialize_aws_json_1_0(value: ProvisionStateEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ProvisionStateEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProvisionStateEnum value: {data!r}")
    return cast(ProvisionStateEnum, data)
