"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListCalculatedAttributeDefinitionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.max_size100
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.token


class ListCalculatedAttributeDefinitionsRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    next_token: NotRequired["capo_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous call to ListCalculatedAttributeDefinitions.</p>"""
    max_results: NotRequired["capo_customer_profiles.types.max_size100.maxSize100"]
    """<p>The maximum number of calculated attribute definitions returned per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCalculatedAttributeDefinitionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCalculatedAttributeDefinitionsRequest:
    out: ListCalculatedAttributeDefinitionsRequest = {}  # type: ignore[typeddict-item]
    return out
