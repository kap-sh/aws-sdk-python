"""Generated from Smithy shape ``com.amazonaws.datazone#FailureReasons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.project_deletion_error

FailureReasons: TypeAlias = list[
    "aws_sdk_datazone.types.project_deletion_error.ProjectDeletionError"
]


# --- restJson1 ser/de ---
def serialize_json(value: FailureReasons) -> list:
    import aws_sdk_datazone.types.project_deletion_error

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.project_deletion_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> FailureReasons:
    import aws_sdk_datazone.types.project_deletion_error

    out: FailureReasons = []
    for item in data:
        out.append(aws_sdk_datazone.types.project_deletion_error.deserialize_json(item))
    return out
