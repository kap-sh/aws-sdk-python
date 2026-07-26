"""Generated from Smithy shape ``com.amazonaws.datazone#FormsInputMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.form_entry_input
    import capo_datazone.types.form_name

FormsInputMap: TypeAlias = dict[
    "capo_datazone.types.form_name.FormName",
    "capo_datazone.types.form_entry_input.FormEntryInput",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FormsInputMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_datazone.types.form_entry_input

        out[key] = capo_datazone.types.form_entry_input.serialize_json(value)
    return out


def deserialize_json(data: dict) -> FormsInputMap:
    out: FormsInputMap = {}
    for key, value in data.items():
        import capo_datazone.types.form_entry_input

        out[key] = capo_datazone.types.form_entry_input.deserialize_json(value)
    return out
