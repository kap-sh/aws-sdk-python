"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#GetPropertyValueHistoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.next_token
    import aws_sdk_iottwinmaker.types.property_value_list


class GetPropertyValueHistoryResponse(TypedDict, closed=True):
    property_values: "aws_sdk_iottwinmaker.types.property_value_list.PropertyValueList"
    """<p>An object that maps strings to the property definitions in the component type. Each string in the mapping must be unique to this object.</p>"""
    next_token: NotRequired["aws_sdk_iottwinmaker.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPropertyValueHistoryResponse) -> dict:
    out: dict = {}
    import aws_sdk_iottwinmaker.types.property_value_list

    out["propertyValues"] = (
        aws_sdk_iottwinmaker.types.property_value_list.serialize_json(
            value["property_values"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetPropertyValueHistoryResponse:
    out: GetPropertyValueHistoryResponse = {}  # type: ignore[typeddict-item]
    if "propertyValues" in data:
        import aws_sdk_iottwinmaker.types.property_value_list

        out["property_values"] = (
            aws_sdk_iottwinmaker.types.property_value_list.deserialize_json(
                data["propertyValues"]
            )
        )
    else:
        raise DeserializationError(
            "GetPropertyValueHistoryResponse.property_values required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
