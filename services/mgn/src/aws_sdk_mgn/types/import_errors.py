"""Generated from Smithy shape ``com.amazonaws.mgn#ImportErrors``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_mgn.types.import_task_error

ImportErrors: TypeAlias = list["aws_sdk_mgn.types.import_task_error.ImportTaskError"]


# --- restJson1 ser/de ---
def serialize_json(value: ImportErrors) -> list:
    import aws_sdk_mgn.types.import_task_error
    out: list = []
    for item in value:
        out.append(aws_sdk_mgn.types.import_task_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImportErrors:
    import aws_sdk_mgn.types.import_task_error
    out: ImportErrors = []
    for item in data:
        out.append(aws_sdk_mgn.types.import_task_error.deserialize_json(item))
    return out