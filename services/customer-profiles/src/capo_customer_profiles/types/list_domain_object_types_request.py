"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListDomainObjectTypesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.max_size100
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.token


class ListDomainObjectTypesRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    max_results: NotRequired["capo_customer_profiles.types.max_size100.maxSize100"]
    """<p>The maximum number of domain object types returned per page.</p>"""
    next_token: NotRequired["capo_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous call to ListDomainObjectTypes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainObjectTypesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDomainObjectTypesRequest:
    out: ListDomainObjectTypesRequest = {}  # type: ignore[typeddict-item]
    return out
