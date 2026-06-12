"""Generated from Smithy shape ``com.amazonaws.fsx#StorageVirtualMachineFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

StorageVirtualMachineFilterName: TypeAlias = Literal["file-system-id",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("file-system-id",))


def serialize_aws_json_1_1(value: StorageVirtualMachineFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StorageVirtualMachineFilterName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown StorageVirtualMachineFilterName value: {data!r}"
        )
    return cast(StorageVirtualMachineFilterName, data)
