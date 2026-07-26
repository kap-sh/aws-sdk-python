"""Generated from Smithy shape ``com.amazonaws.appintegrations#FieldsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appintegrations.types.fields_list
    import capo_appintegrations.types.non_blank_string

FieldsMap: TypeAlias = dict[
    "capo_appintegrations.types.non_blank_string.NonBlankString",
    "capo_appintegrations.types.fields_list.FieldsList",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FieldsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_appintegrations.types.fields_list

        out[key] = capo_appintegrations.types.fields_list.serialize_json(value)
    return out


def deserialize_json(data: dict) -> FieldsMap:
    out: FieldsMap = {}
    for key, value in data.items():
        import capo_appintegrations.types.fields_list

        out[key] = capo_appintegrations.types.fields_list.deserialize_json(value)
    return out
