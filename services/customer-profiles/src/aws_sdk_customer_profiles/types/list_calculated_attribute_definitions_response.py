"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListCalculatedAttributeDefinitionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.calculated_attribute_definitions_list
    import aws_sdk_customer_profiles.types.token


class ListCalculatedAttributeDefinitionsResponse(TypedDict):
    items: NotRequired[
        "aws_sdk_customer_profiles.types.calculated_attribute_definitions_list.CalculatedAttributeDefinitionsList"
    ]
    """<p>The list of calculated attribute definitions.</p>"""
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous call to ListCalculatedAttributeDefinitions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCalculatedAttributeDefinitionsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_customer_profiles.types.calculated_attribute_definitions_list

        out["Items"] = (
            aws_sdk_customer_profiles.types.calculated_attribute_definitions_list.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCalculatedAttributeDefinitionsResponse:
    out: ListCalculatedAttributeDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import aws_sdk_customer_profiles.types.calculated_attribute_definitions_list

        out["items"] = (
            aws_sdk_customer_profiles.types.calculated_attribute_definitions_list.deserialize_json(
                data["Items"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
