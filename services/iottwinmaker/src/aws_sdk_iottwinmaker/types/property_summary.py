"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PropertySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.boolean
    import aws_sdk_iottwinmaker.types.data_value
    import aws_sdk_iottwinmaker.types.name
    import aws_sdk_iottwinmaker.types.property_definition_response


class PropertySummary(TypedDict, closed=True):
    definition: NotRequired[
        "aws_sdk_iottwinmaker.types.property_definition_response.PropertyDefinitionResponse"
    ]
    """<p>This is the schema for the property.</p>"""
    property_name: "aws_sdk_iottwinmaker.types.name.Name"
    """<p>This is the name of the property.</p>"""
    value: NotRequired["aws_sdk_iottwinmaker.types.data_value.DataValue"]
    """<p>This is the value for the property.</p>"""
    are_all_property_values_returned: NotRequired[
        "aws_sdk_iottwinmaker.types.boolean.Boolean"
    ]
    """<p>This flag notes whether all values of a list or map type property are returned in the API response. The maximum number of values per property returned is 50.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropertySummary) -> dict:
    out: dict = {}
    if "definition" in value:
        import aws_sdk_iottwinmaker.types.property_definition_response

        out["definition"] = (
            aws_sdk_iottwinmaker.types.property_definition_response.serialize_json(
                value["definition"]
            )
        )
    out["propertyName"] = value["property_name"]
    if "value" in value:
        import aws_sdk_iottwinmaker.types.data_value

        out["value"] = aws_sdk_iottwinmaker.types.data_value.serialize_json(
            value["value"]
        )
    if "are_all_property_values_returned" in value:
        out["areAllPropertyValuesReturned"] = value["are_all_property_values_returned"]
    return out


def deserialize_json(data: dict) -> PropertySummary:
    out: PropertySummary = {}  # type: ignore[typeddict-item]
    if "definition" in data:
        import aws_sdk_iottwinmaker.types.property_definition_response

        out["definition"] = (
            aws_sdk_iottwinmaker.types.property_definition_response.deserialize_json(
                data["definition"]
            )
        )
    if "propertyName" in data:
        out["property_name"] = data["propertyName"]
    else:
        raise DeserializationError("PropertySummary.property_name required")
    if "value" in data:
        import aws_sdk_iottwinmaker.types.data_value

        out["value"] = aws_sdk_iottwinmaker.types.data_value.deserialize_json(
            data["value"]
        )
    if "areAllPropertyValuesReturned" in data:
        out["are_all_property_values_returned"] = data["areAllPropertyValuesReturned"]
    return out
