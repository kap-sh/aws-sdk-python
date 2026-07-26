"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PropertyLatestValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iottwinmaker.types.data_value
    import capo_iottwinmaker.types.entity_property_reference


class PropertyLatestValue(TypedDict, closed=True):
    property_reference: (
        "capo_iottwinmaker.types.entity_property_reference.EntityPropertyReference"
    )
    """<p>An object that specifies information about a property.</p>"""
    property_value: NotRequired["capo_iottwinmaker.types.data_value.DataValue"]
    """<p>The value of the property.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropertyLatestValue) -> dict:
    out: dict = {}
    import capo_iottwinmaker.types.entity_property_reference

    out["propertyReference"] = (
        capo_iottwinmaker.types.entity_property_reference.serialize_json(
            value["property_reference"]
        )
    )
    if "property_value" in value:
        import capo_iottwinmaker.types.data_value

        out["propertyValue"] = capo_iottwinmaker.types.data_value.serialize_json(
            value["property_value"]
        )
    return out


def deserialize_json(data: dict) -> PropertyLatestValue:
    out: PropertyLatestValue = {}  # type: ignore[typeddict-item]
    if "propertyReference" in data:
        import capo_iottwinmaker.types.entity_property_reference

        out["property_reference"] = (
            capo_iottwinmaker.types.entity_property_reference.deserialize_json(
                data["propertyReference"]
            )
        )
    else:
        raise DeserializationError("PropertyLatestValue.property_reference required")
    if "propertyValue" in data:
        import capo_iottwinmaker.types.data_value

        out["property_value"] = capo_iottwinmaker.types.data_value.deserialize_json(
            data["propertyValue"]
        )
    return out
