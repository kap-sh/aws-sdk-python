"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ProfileAttributeValuesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.attribute_value_item_list
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.status_code
    import capo_customer_profiles.types.string1_to255


class ProfileAttributeValuesResponse(TypedDict, closed=True):
    domain_name: NotRequired["capo_customer_profiles.types.name.name"]
    """<p>The name of the domain.</p>"""
    attribute_name: NotRequired[
        "capo_customer_profiles.types.string1_to255.string1To255"
    ]
    """<p>The attribute name.</p>"""
    items: NotRequired[
        "capo_customer_profiles.types.attribute_value_item_list.AttributeValueItemList"
    ]
    """<p>The items returned as part of the response.</p>"""
    status_code: "capo_customer_profiles.types.status_code.StatusCode"
    """<p>The status code for the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProfileAttributeValuesResponse) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "attribute_name" in value:
        out["AttributeName"] = value["attribute_name"]
    if "items" in value:
        import capo_customer_profiles.types.attribute_value_item_list

        out["Items"] = (
            capo_customer_profiles.types.attribute_value_item_list.serialize_json(
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
        import capo_customer_profiles.types.attribute_value_item_list

        out["items"] = (
            capo_customer_profiles.types.attribute_value_item_list.deserialize_json(
                data["Items"]
            )
        )
    return out
