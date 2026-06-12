"""Generated from Smithy shape ``com.amazonaws.route53#ListCidrCollectionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.pagination_token


class ListCidrCollectionsRequest(TypedDict):
    next_token: NotRequired["aws_sdk_route_53.types.pagination_token.PaginationToken"]
    """<p>An opaque pagination token to indicate where the service is to begin enumerating results.</p> <p>If no value is provided, the listing of results starts from the beginning.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of CIDR collections to return in the response.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListCidrCollectionsRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListCidrCollectionsRequest:
    out: ListCidrCollectionsRequest = {}  # type: ignore[typeddict-item]
    return out
