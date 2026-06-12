"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PropertyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.boolean
    import aws_sdk_iottwinmaker.types.data_value
    import aws_sdk_iottwinmaker.types.property_definition_response


class PropertyResponse(TypedDict):
    definition: NotRequired[
        "aws_sdk_iottwinmaker.types.property_definition_response.PropertyDefinitionResponse"
    ]
    """<p>An object that specifies information about a property.</p>"""
    value: NotRequired["aws_sdk_iottwinmaker.types.data_value.DataValue"]
    """<p>The value of the property.</p>"""
    are_all_property_values_returned: NotRequired[
        "aws_sdk_iottwinmaker.types.boolean.Boolean"
    ]
    """<p>This flag notes whether all values of a list or map type property are returned in the API response. The maximum number of values per property returned is 50.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropertyResponse) -> dict:
    out: dict = {}
    if "definition" in value:
        import aws_sdk_iottwinmaker.types.property_definition_response

        out["definition"] = (
            aws_sdk_iottwinmaker.types.property_definition_response.serialize_json(
                value["definition"]
            )
        )
    if "value" in value:
        import aws_sdk_iottwinmaker.types.data_value

        out["value"] = aws_sdk_iottwinmaker.types.data_value.serialize_json(
            value["value"]
        )
    if "are_all_property_values_returned" in value:
        out["areAllPropertyValuesReturned"] = value["are_all_property_values_returned"]
    return out


def deserialize_json(data: dict) -> PropertyResponse:
    out: PropertyResponse = {}  # type: ignore[typeddict-item]
    if "definition" in data:
        import aws_sdk_iottwinmaker.types.property_definition_response

        out["definition"] = (
            aws_sdk_iottwinmaker.types.property_definition_response.deserialize_json(
                data["definition"]
            )
        )
    if "value" in data:
        import aws_sdk_iottwinmaker.types.data_value

        out["value"] = aws_sdk_iottwinmaker.types.data_value.deserialize_json(
            data["value"]
        )
    if "areAllPropertyValuesReturned" in data:
        out["are_all_property_values_returned"] = data["areAllPropertyValuesReturned"]
    return out
