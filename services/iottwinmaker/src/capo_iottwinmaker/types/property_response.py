"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PropertyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.boolean
    import capo_iottwinmaker.types.data_value
    import capo_iottwinmaker.types.property_definition_response


class PropertyResponse(TypedDict, closed=True):
    definition: NotRequired[
        "capo_iottwinmaker.types.property_definition_response.PropertyDefinitionResponse"
    ]
    """<p>An object that specifies information about a property.</p>"""
    value: NotRequired["capo_iottwinmaker.types.data_value.DataValue"]
    """<p>The value of the property.</p>"""
    are_all_property_values_returned: NotRequired[
        "capo_iottwinmaker.types.boolean.Boolean"
    ]
    """<p>This flag notes whether all values of a list or map type property are returned in the API response. The maximum number of values per property returned is 50.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropertyResponse) -> dict:
    out: dict = {}
    if "definition" in value:
        import capo_iottwinmaker.types.property_definition_response

        out["definition"] = (
            capo_iottwinmaker.types.property_definition_response.serialize_json(
                value["definition"]
            )
        )
    if "value" in value:
        import capo_iottwinmaker.types.data_value

        out["value"] = capo_iottwinmaker.types.data_value.serialize_json(value["value"])
    if "are_all_property_values_returned" in value:
        out["areAllPropertyValuesReturned"] = value["are_all_property_values_returned"]
    return out


def deserialize_json(data: dict) -> PropertyResponse:
    out: PropertyResponse = {}  # type: ignore[typeddict-item]
    if "definition" in data:
        import capo_iottwinmaker.types.property_definition_response

        out["definition"] = (
            capo_iottwinmaker.types.property_definition_response.deserialize_json(
                data["definition"]
            )
        )
    if "value" in data:
        import capo_iottwinmaker.types.data_value

        out["value"] = capo_iottwinmaker.types.data_value.deserialize_json(
            data["value"]
        )
    if "areAllPropertyValuesReturned" in data:
        out["are_all_property_values_returned"] = data["areAllPropertyValuesReturned"]
    return out
