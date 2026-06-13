"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ValueMappings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.form_input_binding_properties
    import aws_sdk_amplifyuibuilder.types.value_mapping_list


class ValueMappings(TypedDict):
    values: "aws_sdk_amplifyuibuilder.types.value_mapping_list.ValueMappingList"
    """<p>The value and display value pairs.</p>"""
    binding_properties: NotRequired[
        "aws_sdk_amplifyuibuilder.types.form_input_binding_properties.FormInputBindingProperties"
    ]
    """<p>The information to bind fields to data at runtime.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValueMappings) -> dict:
    out: dict = {}
    import aws_sdk_amplifyuibuilder.types.value_mapping_list

    out["values"] = aws_sdk_amplifyuibuilder.types.value_mapping_list.serialize_json(
        value["values"]
    )
    if "binding_properties" in value:
        import aws_sdk_amplifyuibuilder.types.form_input_binding_properties

        out["bindingProperties"] = (
            aws_sdk_amplifyuibuilder.types.form_input_binding_properties.serialize_json(
                value["binding_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValueMappings:
    out: ValueMappings = {}  # type: ignore[typeddict-item]
    if "values" in data:
        import aws_sdk_amplifyuibuilder.types.value_mapping_list

        out["values"] = (
            aws_sdk_amplifyuibuilder.types.value_mapping_list.deserialize_json(
                data["values"]
            )
        )
    else:
        raise DeserializationError("ValueMappings.values required")
    if "bindingProperties" in data:
        import aws_sdk_amplifyuibuilder.types.form_input_binding_properties

        out["binding_properties"] = (
            aws_sdk_amplifyuibuilder.types.form_input_binding_properties.deserialize_json(
                data["bindingProperties"]
            )
        )
    return out
