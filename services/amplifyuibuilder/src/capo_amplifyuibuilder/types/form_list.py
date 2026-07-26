"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FormList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.form

FormList: TypeAlias = list["capo_amplifyuibuilder.types.form.Form"]


# --- restJson1 ser/de ---
def serialize_json(value: FormList) -> list:
    import capo_amplifyuibuilder.types.form

    out: list = []
    for item in value:
        out.append(capo_amplifyuibuilder.types.form.serialize_json(item))
    return out


def deserialize_json(data: list) -> FormList:
    import capo_amplifyuibuilder.types.form

    out: FormList = []
    for item in data:
        out.append(capo_amplifyuibuilder.types.form.deserialize_json(item))
    return out
