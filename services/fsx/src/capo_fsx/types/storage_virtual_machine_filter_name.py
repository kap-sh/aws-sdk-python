"""Generated from Smithy shape ``com.amazonaws.fsx#StorageVirtualMachineFilterName``."""

from typing import Literal, TypeAlias, cast

StorageVirtualMachineFilterName: TypeAlias = Literal["file-system-id",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StorageVirtualMachineFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StorageVirtualMachineFilterName:
    return cast(StorageVirtualMachineFilterName, data)
