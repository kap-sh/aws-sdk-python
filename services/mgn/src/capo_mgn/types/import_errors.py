"""Generated from Smithy shape ``com.amazonaws.mgn#ImportErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.import_task_error

ImportErrors: TypeAlias = list["capo_mgn.types.import_task_error.ImportTaskError"]


# --- restJson1 ser/de ---
def serialize_json(value: ImportErrors) -> list:
    import capo_mgn.types.import_task_error

    out: list = []
    for item in value:
        out.append(capo_mgn.types.import_task_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImportErrors:
    import capo_mgn.types.import_task_error

    out: ImportErrors = []
    for item in data:
        out.append(capo_mgn.types.import_task_error.deserialize_json(item))
    return out
