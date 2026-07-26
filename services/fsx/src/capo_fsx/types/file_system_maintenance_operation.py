"""Generated from Smithy shape ``com.amazonaws.fsx#FileSystemMaintenanceOperation``."""

from typing import Literal, TypeAlias, cast

"""<p>An enumeration specifying the currently ongoing maintenance operation.</p>"""
FileSystemMaintenanceOperation: TypeAlias = Literal[
    "PATCHING",
    "BACKING_UP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileSystemMaintenanceOperation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FileSystemMaintenanceOperation:
    return cast(FileSystemMaintenanceOperation, data)
