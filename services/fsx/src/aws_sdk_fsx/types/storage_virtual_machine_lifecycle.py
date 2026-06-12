"""Generated from Smithy shape ``com.amazonaws.fsx#StorageVirtualMachineLifecycle``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

StorageVirtualMachineLifecycle: TypeAlias = Literal[
    "CREATED",
    "CREATING",
    "DELETING",
    "FAILED",
    "MISCONFIGURED",
    "PENDING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED",
        "CREATING",
        "DELETING",
        "FAILED",
        "MISCONFIGURED",
        "PENDING",
    )
)


def serialize_aws_json_1_1(value: StorageVirtualMachineLifecycle) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StorageVirtualMachineLifecycle:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown StorageVirtualMachineLifecycle value: {data!r}"
        )
    return cast(StorageVirtualMachineLifecycle, data)
