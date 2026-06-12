"""Generated from Smithy shape ``com.amazonaws.fsx#FileSystemMaintenanceOperation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

"""<p>An enumeration specifying the currently ongoing maintenance operation.</p>"""
FileSystemMaintenanceOperation: TypeAlias = Literal[
    "PATCHING",
    "BACKING_UP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PATCHING",
        "BACKING_UP",
    )
)


def serialize_aws_json_1_1(value: FileSystemMaintenanceOperation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FileSystemMaintenanceOperation:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown FileSystemMaintenanceOperation value: {data!r}"
        )
    return cast(FileSystemMaintenanceOperation, data)
