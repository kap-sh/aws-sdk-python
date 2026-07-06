"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FormInputBindingPropertiesValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.form_input_binding_properties_value_properties


class FormInputBindingPropertiesValue(TypedDict, closed=True):
    type: NotRequired["str"]
    """<p>The property type.</p>"""
    binding_properties: NotRequired[
        "aws_sdk_amplifyuibuilder.types.form_input_binding_properties_value_properties.FormInputBindingPropertiesValueProperties"
    ]
    """<p>Describes the properties to customize with data at runtime.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormInputBindingPropertiesValue) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "binding_properties" in value:
        import aws_sdk_amplifyuibuilder.types.form_input_binding_properties_value_properties

        out["bindingProperties"] = (
            aws_sdk_amplifyuibuilder.types.form_input_binding_properties_value_properties.serialize_json(
                value["binding_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> FormInputBindingPropertiesValue:
    out: FormInputBindingPropertiesValue = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    if "bindingProperties" in data:
        import aws_sdk_amplifyuibuilder.types.form_input_binding_properties_value_properties

        out["binding_properties"] = (
            aws_sdk_amplifyuibuilder.types.form_input_binding_properties_value_properties.deserialize_json(
                data["bindingProperties"]
            )
        )
    return out
