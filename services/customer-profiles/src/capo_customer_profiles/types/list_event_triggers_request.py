"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListEventTriggersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.max_size100
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.token


class ListEventTriggersRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    next_token: NotRequired["capo_customer_profiles.types.token.token"]
    """<p>The pagination token to use with ListEventTriggers.</p>"""
    max_results: NotRequired["capo_customer_profiles.types.max_size100.maxSize100"]
    """<p>The maximum number of results to return per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventTriggersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEventTriggersRequest:
    out: ListEventTriggersRequest = {}  # type: ignore[typeddict-item]
    return out
