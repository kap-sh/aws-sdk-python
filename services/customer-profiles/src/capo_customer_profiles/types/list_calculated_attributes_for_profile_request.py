"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListCalculatedAttributesForProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.max_size100
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.token
    import capo_customer_profiles.types.uuid


class ListCalculatedAttributesForProfileRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous call to ListCalculatedAttributesForProfile.</p>"""
    max_results: NotRequired["capo_customer_profiles.types.max_size100.maxSize100"]
    """<p>The maximum number of calculated attributes returned per page.</p>"""
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    profile_id: "capo_customer_profiles.types.uuid.uuid"
    """<p>The unique identifier of a customer profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCalculatedAttributesForProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCalculatedAttributesForProfileRequest:
    out: ListCalculatedAttributesForProfileRequest = {}  # type: ignore[typeddict-item]
    return out
