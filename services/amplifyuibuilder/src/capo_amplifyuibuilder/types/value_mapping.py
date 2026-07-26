"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ValueMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.form_input_value_property


class ValueMapping(TypedDict, closed=True):
    display_value: NotRequired[
        "capo_amplifyuibuilder.types.form_input_value_property.FormInputValueProperty"
    ]
    """<p>The value to display for the complex object.</p>"""
    value: (
        "capo_amplifyuibuilder.types.form_input_value_property.FormInputValueProperty"
    )
    """<p>The complex object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValueMapping) -> dict:
    out: dict = {}
    if "display_value" in value:
        import capo_amplifyuibuilder.types.form_input_value_property

        out["displayValue"] = (
            capo_amplifyuibuilder.types.form_input_value_property.serialize_json(
                value["display_value"]
            )
        )
    import capo_amplifyuibuilder.types.form_input_value_property

    out["value"] = capo_amplifyuibuilder.types.form_input_value_property.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> ValueMapping:
    out: ValueMapping = {}  # type: ignore[typeddict-item]
    if "displayValue" in data:
        import capo_amplifyuibuilder.types.form_input_value_property

        out["display_value"] = (
            capo_amplifyuibuilder.types.form_input_value_property.deserialize_json(
                data["displayValue"]
            )
        )
    if "value" in data:
        import capo_amplifyuibuilder.types.form_input_value_property

        out["value"] = (
            capo_amplifyuibuilder.types.form_input_value_property.deserialize_json(
                data["value"]
            )
        )
    else:
        raise DeserializationError("ValueMapping.value required")
    return out
