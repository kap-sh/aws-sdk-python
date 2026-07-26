"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FormBindings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.form_binding_element

FormBindings: TypeAlias = dict[
    "str", "capo_amplifyuibuilder.types.form_binding_element.FormBindingElement"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FormBindings) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_amplifyuibuilder.types.form_binding_element

        out[key] = capo_amplifyuibuilder.types.form_binding_element.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> FormBindings:
    out: FormBindings = {}
    for key, value in data.items():
        import capo_amplifyuibuilder.types.form_binding_element

        out[key] = capo_amplifyuibuilder.types.form_binding_element.deserialize_json(
            value
        )
    return out
