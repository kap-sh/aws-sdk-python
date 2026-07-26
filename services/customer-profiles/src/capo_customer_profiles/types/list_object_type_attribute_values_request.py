"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListObjectTypeAttributeValuesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.max_size100
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.string1_to1000
    import capo_customer_profiles.types.token
    import capo_customer_profiles.types.type_name


class ListObjectTypeAttributeValuesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous call.</p>"""
    max_results: NotRequired["capo_customer_profiles.types.max_size100.maxSize100"]
    """<p>The maximum number of objects returned per page. Valid Range: Minimum value of 1. Maximum value of 100. If not provided default as 100.</p>"""
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    object_type_name: "capo_customer_profiles.types.type_name.typeName"
    """<p>The unique name of the domain object type.</p>"""
    attribute_name: "capo_customer_profiles.types.string1_to1000.string1To1000"
    """<p>The attribute name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListObjectTypeAttributeValuesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListObjectTypeAttributeValuesRequest:
    out: ListObjectTypeAttributeValuesRequest = {}  # type: ignore[typeddict-item]
    return out
