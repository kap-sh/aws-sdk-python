"""Generated from Smithy shape ``com.amazonaws.connect#RequiredTaskTemplateFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.required_field_info

RequiredTaskTemplateFields: TypeAlias = list[
    "capo_connect.types.required_field_info.RequiredFieldInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: RequiredTaskTemplateFields) -> list:
    import capo_connect.types.required_field_info

    out: list = []
    for item in value:
        out.append(capo_connect.types.required_field_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> RequiredTaskTemplateFields:
    import capo_connect.types.required_field_info

    out: RequiredTaskTemplateFields = []
    for item in data:
        out.append(capo_connect.types.required_field_info.deserialize_json(item))
    return out
