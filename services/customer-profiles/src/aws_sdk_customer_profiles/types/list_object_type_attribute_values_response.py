"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListObjectTypeAttributeValuesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.list_object_type_attribute_values_list
    import aws_sdk_customer_profiles.types.token


class ListObjectTypeAttributeValuesResponse(TypedDict, closed=True):
    items: NotRequired[
        "aws_sdk_customer_profiles.types.list_object_type_attribute_values_list.ListObjectTypeAttributeValuesList"
    ]
    """<p>A list of unique attribute values sorted on the basis of LastUpdatedAt. </p>"""
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous call to call ListObjectTypeAttributeValues. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListObjectTypeAttributeValuesResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_customer_profiles.types.list_object_type_attribute_values_list

        out["Items"] = (
            aws_sdk_customer_profiles.types.list_object_type_attribute_values_list.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListObjectTypeAttributeValuesResponse:
    out: ListObjectTypeAttributeValuesResponse = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import aws_sdk_customer_profiles.types.list_object_type_attribute_values_list

        out["items"] = (
            aws_sdk_customer_profiles.types.list_object_type_attribute_values_list.deserialize_json(
                data["Items"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
