"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#GetPropertyValueResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.next_token
    import aws_sdk_iottwinmaker.types.property_latest_value_map
    import aws_sdk_iottwinmaker.types.tabular_property_values


class GetPropertyValueResponse(TypedDict, closed=True):
    property_values: NotRequired[
        "aws_sdk_iottwinmaker.types.property_latest_value_map.PropertyLatestValueMap"
    ]
    """<p>An object that maps strings to the properties and latest property values in the response. Each string in the mapping must be unique to this object.</p>"""
    next_token: NotRequired["aws_sdk_iottwinmaker.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results.</p>"""
    tabular_property_values: NotRequired[
        "aws_sdk_iottwinmaker.types.tabular_property_values.TabularPropertyValues"
    ]
    """<p>A table of property values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPropertyValueResponse) -> dict:
    out: dict = {}
    if "property_values" in value:
        import aws_sdk_iottwinmaker.types.property_latest_value_map

        out["propertyValues"] = (
            aws_sdk_iottwinmaker.types.property_latest_value_map.serialize_json(
                value["property_values"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "tabular_property_values" in value:
        import aws_sdk_iottwinmaker.types.tabular_property_values

        out["tabularPropertyValues"] = (
            aws_sdk_iottwinmaker.types.tabular_property_values.serialize_json(
                value["tabular_property_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetPropertyValueResponse:
    out: GetPropertyValueResponse = {}  # type: ignore[typeddict-item]
    if "propertyValues" in data:
        import aws_sdk_iottwinmaker.types.property_latest_value_map

        out["property_values"] = (
            aws_sdk_iottwinmaker.types.property_latest_value_map.deserialize_json(
                data["propertyValues"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "tabularPropertyValues" in data:
        import aws_sdk_iottwinmaker.types.tabular_property_values

        out["tabular_property_values"] = (
            aws_sdk_iottwinmaker.types.tabular_property_values.deserialize_json(
                data["tabularPropertyValues"]
            )
        )
    return out
