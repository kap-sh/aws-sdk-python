"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FormInputValuePropertyBindingProperties``."""

from typing_extensions import NotRequired, TypedDict

from aws_sdk_amplifyuibuilder.errors import DeserializationError


class FormInputValuePropertyBindingProperties(TypedDict, closed=True):
    property: "str"
    """<p>The form property to bind to the data field.</p>"""
    field: NotRequired["str"]
    """<p>The data field to bind the property to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormInputValuePropertyBindingProperties) -> dict:
    out: dict = {}
    out["property"] = value["property"]
    if "field" in value:
        out["field"] = value["field"]
    return out


def deserialize_json(data: dict) -> FormInputValuePropertyBindingProperties:
    out: FormInputValuePropertyBindingProperties = {}  # type: ignore[typeddict-item]
    if "property" in data:
        out["property"] = data["property"]
    else:
        raise DeserializationError(
            "FormInputValuePropertyBindingProperties.property required"
        )
    if "field" in data:
        out["field"] = data["field"]
    return out
