"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListObjectTypeAttributeValuesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.max_size100
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.string1_to1000
    import aws_sdk_customer_profiles.types.token
    import aws_sdk_customer_profiles.types.type_name


class ListObjectTypeAttributeValuesRequest(TypedDict):
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous call.</p>"""
    max_results: NotRequired["aws_sdk_customer_profiles.types.max_size100.maxSize100"]
    """<p>The maximum number of objects returned per page. Valid Range: Minimum value of 1. Maximum value of 100. If not provided default as 100.</p>"""
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    object_type_name: "aws_sdk_customer_profiles.types.type_name.typeName"
    """<p>The unique name of the domain object type.</p>"""
    attribute_name: "aws_sdk_customer_profiles.types.string1_to1000.string1To1000"
    """<p>The attribute name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListObjectTypeAttributeValuesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListObjectTypeAttributeValuesRequest:
    out: ListObjectTypeAttributeValuesRequest = {}  # type: ignore[typeddict-item]
    return out
