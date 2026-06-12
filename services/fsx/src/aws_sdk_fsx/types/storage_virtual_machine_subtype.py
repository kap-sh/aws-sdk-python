"""Generated from Smithy shape ``com.amazonaws.fsx#StorageVirtualMachineSubtype``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

StorageVirtualMachineSubtype: TypeAlias = Literal[
    "DEFAULT",
    "DP_DESTINATION",
    "SYNC_DESTINATION",
    "SYNC_SOURCE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT",
        "DP_DESTINATION",
        "SYNC_DESTINATION",
        "SYNC_SOURCE",
    )
)


def serialize_aws_json_1_1(value: StorageVirtualMachineSubtype) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StorageVirtualMachineSubtype:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown StorageVirtualMachineSubtype value: {data!r}"
        )
    return cast(StorageVirtualMachineSubtype, data)
