"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ComponentBindingPropertiesValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.component_binding_properties_value_properties


class ComponentBindingPropertiesValue(TypedDict, closed=True):
    type: NotRequired["str"]
    """<p>The property type.</p>"""
    binding_properties: NotRequired[
        "aws_sdk_amplifyuibuilder.types.component_binding_properties_value_properties.ComponentBindingPropertiesValueProperties"
    ]
    """<p>Describes the properties to customize with data at runtime.</p>"""
    default_value: NotRequired["str"]
    """<p>The default value of the property.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentBindingPropertiesValue) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "binding_properties" in value:
        import aws_sdk_amplifyuibuilder.types.component_binding_properties_value_properties

        out["bindingProperties"] = (
            aws_sdk_amplifyuibuilder.types.component_binding_properties_value_properties.serialize_json(
                value["binding_properties"]
            )
        )
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    return out


def deserialize_json(data: dict) -> ComponentBindingPropertiesValue:
    out: ComponentBindingPropertiesValue = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    if "bindingProperties" in data:
        import aws_sdk_amplifyuibuilder.types.component_binding_properties_value_properties

        out["binding_properties"] = (
            aws_sdk_amplifyuibuilder.types.component_binding_properties_value_properties.deserialize_json(
                data["bindingProperties"]
            )
        )
    if "defaultValue" in data:
        out["default_value"] = data["defaultValue"]
    return out
