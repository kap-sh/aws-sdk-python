"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListProfileObjectTypesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.max_size100
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.token


class ListProfileObjectTypesRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    next_token: NotRequired["capo_customer_profiles.types.token.token"]
    """<p>Identifies the next page of results to return.</p>"""
    max_results: NotRequired["capo_customer_profiles.types.max_size100.maxSize100"]
    """<p>The maximum number of objects returned per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProfileObjectTypesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListProfileObjectTypesRequest:
    out: ListProfileObjectTypesRequest = {}  # type: ignore[typeddict-item]
    return out
