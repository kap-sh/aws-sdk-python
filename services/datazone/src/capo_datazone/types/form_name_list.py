"""Generated from Smithy shape ``com.amazonaws.datazone#FormNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.form_name

FormNameList: TypeAlias = list["capo_datazone.types.form_name.FormName"]


# --- restJson1 ser/de ---
def serialize_json(value: FormNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> FormNameList:
    return list(data)
