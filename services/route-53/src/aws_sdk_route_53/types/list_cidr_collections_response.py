"""Generated from Smithy shape ``com.amazonaws.route53#ListCidrCollectionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.collection_summaries
    import aws_sdk_route_53.types.pagination_token


class ListCidrCollectionsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_route_53.types.pagination_token.PaginationToken"]
    """<p>An opaque pagination token to indicate where the service is to begin enumerating results.</p> <p>If no value is provided, the listing of results starts from the beginning.</p>"""
    cidr_collections: NotRequired[
        "aws_sdk_route_53.types.collection_summaries.CollectionSummaries"
    ]
    """<p>A complex type with information about the CIDR collection.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListCidrCollectionsResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "next_token" in value:
        SubElement(el, "NextToken").text = str(value["next_token"])
    if "cidr_collections" in value:
        import aws_sdk_route_53.types.collection_summaries

        aws_sdk_route_53.types.collection_summaries.serialize_xml(
            value["cidr_collections"], el, "CidrCollections"
        )


def deserialize_xml(el: Element) -> ListCidrCollectionsResponse:
    out: ListCidrCollectionsResponse = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_cidr_collections = el.find("CidrCollections")
    if child_cidr_collections is not None:
        import aws_sdk_route_53.types.collection_summaries

        out["cidr_collections"] = (
            aws_sdk_route_53.types.collection_summaries.deserialize_xml(
                child_cidr_collections
            )
        )
    return out
