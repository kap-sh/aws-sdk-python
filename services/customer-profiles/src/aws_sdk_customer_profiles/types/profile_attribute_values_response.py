"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ProfileAttributeValuesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.attribute_value_item_list
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.status_code
    import aws_sdk_customer_profiles.types.string1_to255


class ProfileAttributeValuesResponse(TypedDict):
    domain_name: NotRequired["aws_sdk_customer_profiles.types.name.name"]
    """<p>The name of the domain.</p>"""
    attribute_name: NotRequired[
        "aws_sdk_customer_profiles.types.string1_to255.string1To255"
    ]
    """<p>The attribute name.</p>"""
    items: NotRequired[
        "aws_sdk_customer_profiles.types.attribute_value_item_list.AttributeValueItemList"
    ]
    """<p>The items returned as part of the response.</p>"""
    status_code: "aws_sdk_customer_profiles.types.status_code.StatusCode"
    """<p>The status code for the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProfileAttributeValuesResponse) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "attribute_name" in value:
        out["AttributeName"] = value["attribute_name"]
    if "items" in value:
        import aws_sdk_customer_profiles.types.attribute_value_item_list

        out["Items"] = (
            aws_sdk_customer_profiles.types.attribute_value_item_list.serialize_json(
                value["items"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProfileAttributeValuesResponse:
    out: ProfileAttributeValuesResponse = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    if "Items" in data:
        import aws_sdk_customer_profiles.types.attribute_value_item_list

        out["items"] = (
            aws_sdk_customer_profiles.types.attribute_value_item_list.deserialize_json(
                data["Items"]
            )
        )
    return out
