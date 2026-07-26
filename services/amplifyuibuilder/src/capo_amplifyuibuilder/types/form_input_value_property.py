"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FormInputValueProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.form_input_value_property_binding_properties
    import capo_amplifyuibuilder.types.form_input_value_property_list


class FormInputValueProperty(TypedDict, closed=True):
    value: NotRequired["str"]
    """<p>The value to assign to the input field.</p>"""
    binding_properties: NotRequired[
        "capo_amplifyuibuilder.types.form_input_value_property_binding_properties.FormInputValuePropertyBindingProperties"
    ]
    """<p>The information to bind fields to data at runtime.</p>"""
    concat: NotRequired[
        "capo_amplifyuibuilder.types.form_input_value_property_list.FormInputValuePropertyList"
    ]
    """<p>A list of form properties to concatenate to create the value to assign to this field property.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormInputValueProperty) -> dict:
    out: dict = {}
    if "value" in value:
        out["value"] = value["value"]
    if "binding_properties" in value:
        import capo_amplifyuibuilder.types.form_input_value_property_binding_properties

        out["bindingProperties"] = (
            capo_amplifyuibuilder.types.form_input_value_property_binding_properties.serialize_json(
                value["binding_properties"]
            )
        )
    if "concat" in value:
        import capo_amplifyuibuilder.types.form_input_value_property_list

        out["concat"] = (
            capo_amplifyuibuilder.types.form_input_value_property_list.serialize_json(
                value["concat"]
            )
        )
    return out


def deserialize_json(data: dict) -> FormInputValueProperty:
    out: FormInputValueProperty = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    if "bindingProperties" in data:
        import capo_amplifyuibuilder.types.form_input_value_property_binding_properties

        out["binding_properties"] = (
            capo_amplifyuibuilder.types.form_input_value_property_binding_properties.deserialize_json(
                data["bindingProperties"]
            )
        )
    if "concat" in data:
        import capo_amplifyuibuilder.types.form_input_value_property_list

        out["concat"] = (
            capo_amplifyuibuilder.types.form_input_value_property_list.deserialize_json(
                data["concat"]
            )
        )
    return out
