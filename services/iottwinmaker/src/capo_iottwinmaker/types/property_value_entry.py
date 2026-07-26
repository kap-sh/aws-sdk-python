"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PropertyValueEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iottwinmaker.types.entity_property_reference
    import capo_iottwinmaker.types.property_values


class PropertyValueEntry(TypedDict, closed=True):
    entity_property_reference: (
        "capo_iottwinmaker.types.entity_property_reference.EntityPropertyReference"
    )
    """<p>An object that contains information about the entity that has the property.</p>"""
    property_values: NotRequired[
        "capo_iottwinmaker.types.property_values.PropertyValues"
    ]
    """<p>A list of objects that specify time series property values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropertyValueEntry) -> dict:
    out: dict = {}
    import capo_iottwinmaker.types.entity_property_reference

    out["entityPropertyReference"] = (
        capo_iottwinmaker.types.entity_property_reference.serialize_json(
            value["entity_property_reference"]
        )
    )
    if "property_values" in value:
        import capo_iottwinmaker.types.property_values

        out["propertyValues"] = capo_iottwinmaker.types.property_values.serialize_json(
            value["property_values"]
        )
    return out


def deserialize_json(data: dict) -> PropertyValueEntry:
    out: PropertyValueEntry = {}  # type: ignore[typeddict-item]
    if "entityPropertyReference" in data:
        import capo_iottwinmaker.types.entity_property_reference

        out["entity_property_reference"] = (
            capo_iottwinmaker.types.entity_property_reference.deserialize_json(
                data["entityPropertyReference"]
            )
        )
    else:
        raise DeserializationError(
            "PropertyValueEntry.entity_property_reference required"
        )
    if "propertyValues" in data:
        import capo_iottwinmaker.types.property_values

        out["property_values"] = (
            capo_iottwinmaker.types.property_values.deserialize_json(
                data["propertyValues"]
            )
        )
    return out
