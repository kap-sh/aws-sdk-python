"""Generated from Smithy shape ``com.amazonaws.route53#ListCidrBlocksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.cidr_location_name_default_not_allowed
    import capo_route_53.types.pagination_token
    import capo_route_53.types.uuid


class ListCidrBlocksRequest(TypedDict, closed=True):
    collection_id: "capo_route_53.types.uuid.UUID"
    """<p>The UUID of the CIDR collection.</p>"""
    location_name: NotRequired[
        "capo_route_53.types.cidr_location_name_default_not_allowed.CidrLocationNameDefaultNotAllowed"
    ]
    """<p>The name of the CIDR collection location.</p>"""
    next_token: NotRequired["capo_route_53.types.pagination_token.PaginationToken"]
    """<p>An opaque pagination token to indicate where the service is to begin enumerating results.</p>"""
    max_results: NotRequired["int"]
    """<p>Maximum number of results you want returned.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListCidrBlocksRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListCidrBlocksRequest:
    out: ListCidrBlocksRequest = {}  # type: ignore[typeddict-item]
    return out
