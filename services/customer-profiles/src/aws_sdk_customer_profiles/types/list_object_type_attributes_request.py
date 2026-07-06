"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListObjectTypeAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.max_size100
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.token
    import aws_sdk_customer_profiles.types.type_name


class ListObjectTypeAttributesRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous call. </p>"""
    max_results: NotRequired["aws_sdk_customer_profiles.types.max_size100.maxSize100"]
    """<p>The maximum number of objects returned per page.</p>"""
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique identifier of the domain.</p>"""
    object_type_name: "aws_sdk_customer_profiles.types.type_name.typeName"
    """<p>The name of the profile object type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListObjectTypeAttributesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListObjectTypeAttributesRequest:
    out: ListObjectTypeAttributesRequest = {}  # type: ignore[typeddict-item]
    return out
