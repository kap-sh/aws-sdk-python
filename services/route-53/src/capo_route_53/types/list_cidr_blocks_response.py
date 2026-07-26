"""Generated from Smithy shape ``com.amazonaws.route53#ListCidrBlocksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.cidr_block_summaries
    import capo_route_53.types.pagination_token


class ListCidrBlocksResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_route_53.types.pagination_token.PaginationToken"]
    """<p>An opaque pagination token to indicate where the service is to begin enumerating results. </p> <p>If no value is provided, the listing of results starts from the beginning.</p>"""
    cidr_blocks: NotRequired[
        "capo_route_53.types.cidr_block_summaries.CidrBlockSummaries"
    ]
    """<p>A complex type that contains information about the CIDR blocks.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListCidrBlocksResponse, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "next_token" in value:
        SubElement(el, "NextToken").text = str(value["next_token"])
    if "cidr_blocks" in value:
        import capo_route_53.types.cidr_block_summaries

        capo_route_53.types.cidr_block_summaries.serialize_xml(
            value["cidr_blocks"], el, "CidrBlocks"
        )


def deserialize_xml(el: Element) -> ListCidrBlocksResponse:
    out: ListCidrBlocksResponse = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_cidr_blocks = el.find("CidrBlocks")
    if child_cidr_blocks is not None:
        import capo_route_53.types.cidr_block_summaries

        out["cidr_blocks"] = capo_route_53.types.cidr_block_summaries.deserialize_xml(
            child_cidr_blocks
        )
    return out
