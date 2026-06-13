"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#MutationActionSetStateParameter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.component_property


class MutationActionSetStateParameter(TypedDict):
    component_name: "str"
    """<p>The name of the component that is being modified.</p>"""
    property: "str"
    """<p>The name of the component property to apply the state configuration to.</p>"""
    set: "aws_sdk_amplifyuibuilder.types.component_property.ComponentProperty"
    """<p>The state configuration to assign to the property.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MutationActionSetStateParameter) -> dict:
    out: dict = {}
    out["componentName"] = value["component_name"]
    out["property"] = value["property"]
    import aws_sdk_amplifyuibuilder.types.component_property

    out["set"] = aws_sdk_amplifyuibuilder.types.component_property.serialize_json(
        value["set"]
    )
    return out


def deserialize_json(data: dict) -> MutationActionSetStateParameter:
    out: MutationActionSetStateParameter = {}  # type: ignore[typeddict-item]
    if "componentName" in data:
        out["component_name"] = data["componentName"]
    else:
        raise DeserializationError(
            "MutationActionSetStateParameter.component_name required"
        )
    if "property" in data:
        out["property"] = data["property"]
    else:
        raise DeserializationError("MutationActionSetStateParameter.property required")
    if "set" in data:
        import aws_sdk_amplifyuibuilder.types.component_property

        out["set"] = aws_sdk_amplifyuibuilder.types.component_property.deserialize_json(
            data["set"]
        )
    else:
        raise DeserializationError("MutationActionSetStateParameter.set required")
    return out
