"""Generated from Smithy shape ``com.amazonaws.connectcases#RequiredFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.required_field

RequiredFieldList: TypeAlias = list[
    "capo_connectcases.types.required_field.RequiredField"
]


# --- restJson1 ser/de ---
def serialize_json(value: RequiredFieldList) -> list:
    import capo_connectcases.types.required_field

    out: list = []
    for item in value:
        out.append(capo_connectcases.types.required_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> RequiredFieldList:
    import capo_connectcases.types.required_field

    out: RequiredFieldList = []
    for item in data:
        out.append(capo_connectcases.types.required_field.deserialize_json(item))
    return out
