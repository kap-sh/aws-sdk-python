"""Generated from Smithy shape ``com.amazonaws.opensearch#ListDataSourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.domain_name


class ListDataSourcesRequest(TypedDict, closed=True):
    domain_name: "capo_opensearch.types.domain_name.DomainName"
    """<p>The name of the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataSourcesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDataSourcesRequest:
    out: ListDataSourcesRequest = {}  # type: ignore[typeddict-item]
    return out
