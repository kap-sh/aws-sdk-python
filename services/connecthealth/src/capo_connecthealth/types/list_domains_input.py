"""Generated from Smithy shape ``com.amazonaws.connecthealth#ListDomainsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.domain_status


class ListDomainsInput(TypedDict, closed=True):
    status: NotRequired["capo_connecthealth.types.domain_status.DomainStatus"]
    """<p>Filter by Domain status.</p>"""
    max_results: NotRequired["int"]
    """<p>Maximum number of results to return.</p>"""
    next_token: NotRequired["str"]
    """<p>Token for pagination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDomainsInput:
    out: ListDomainsInput = {}  # type: ignore[typeddict-item]
    return out
