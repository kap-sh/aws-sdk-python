"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListObjectTypeAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.max_size100
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.token
    import capo_customer_profiles.types.type_name


class ListObjectTypeAttributesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous call. </p>"""
    max_results: NotRequired["capo_customer_profiles.types.max_size100.maxSize100"]
    """<p>The maximum number of objects returned per page.</p>"""
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique identifier of the domain.</p>"""
    object_type_name: "capo_customer_profiles.types.type_name.typeName"
    """<p>The name of the profile object type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListObjectTypeAttributesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListObjectTypeAttributesRequest:
    out: ListObjectTypeAttributesRequest = {}  # type: ignore[typeddict-item]
    return out
