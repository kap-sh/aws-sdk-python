"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PropertyLatestValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.data_value
    import aws_sdk_iottwinmaker.types.entity_property_reference


class PropertyLatestValue(TypedDict):
    property_reference: (
        "aws_sdk_iottwinmaker.types.entity_property_reference.EntityPropertyReference"
    )
    """<p>An object that specifies information about a property.</p>"""
    property_value: NotRequired["aws_sdk_iottwinmaker.types.data_value.DataValue"]
    """<p>The value of the property.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropertyLatestValue) -> dict:
    out: dict = {}
    import aws_sdk_iottwinmaker.types.entity_property_reference

    out["propertyReference"] = (
        aws_sdk_iottwinmaker.types.entity_property_reference.serialize_json(
            value["property_reference"]
        )
    )
    if "property_value" in value:
        import aws_sdk_iottwinmaker.types.data_value

        out["propertyValue"] = aws_sdk_iottwinmaker.types.data_value.serialize_json(
            value["property_value"]
        )
    return out


def deserialize_json(data: dict) -> PropertyLatestValue:
    out: PropertyLatestValue = {}  # type: ignore[typeddict-item]
    if "propertyReference" in data:
        import aws_sdk_iottwinmaker.types.entity_property_reference

        out["property_reference"] = (
            aws_sdk_iottwinmaker.types.entity_property_reference.deserialize_json(
                data["propertyReference"]
            )
        )
    else:
        raise DeserializationError("PropertyLatestValue.property_reference required")
    if "propertyValue" in data:
        import aws_sdk_iottwinmaker.types.data_value

        out["property_value"] = aws_sdk_iottwinmaker.types.data_value.deserialize_json(
            data["propertyValue"]
        )
    return out
