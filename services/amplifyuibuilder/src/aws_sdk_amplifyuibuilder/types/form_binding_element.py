"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FormBindingElement``."""

from typing_extensions import TypedDict

from aws_sdk_amplifyuibuilder.errors import DeserializationError


class FormBindingElement(TypedDict, closed=True):
    element: "str"
    """<p>The name of the component to retrieve a value from.</p>"""
    property: "str"
    """<p>The property to retrieve a value from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormBindingElement) -> dict:
    out: dict = {}
    out["element"] = value["element"]
    out["property"] = value["property"]
    return out


def deserialize_json(data: dict) -> FormBindingElement:
    out: FormBindingElement = {}  # type: ignore[typeddict-item]
    if "element" in data:
        out["element"] = data["element"]
    else:
        raise DeserializationError("FormBindingElement.element required")
    if "property" in data:
        out["property"] = data["property"]
    else:
        raise DeserializationError("FormBindingElement.property required")
    return out
