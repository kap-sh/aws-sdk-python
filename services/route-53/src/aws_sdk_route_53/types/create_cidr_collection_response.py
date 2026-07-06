"""Generated from Smithy shape ``com.amazonaws.route53#CreateCidrCollectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.cidr_collection
    import aws_sdk_route_53.types.resource_uri


class CreateCidrCollectionResponse(TypedDict, closed=True):
    collection: NotRequired["aws_sdk_route_53.types.cidr_collection.CidrCollection"]
    """<p>A complex type that contains information about the CIDR collection.</p>"""
    location: NotRequired["aws_sdk_route_53.types.resource_uri.ResourceURI"]
    """<p>A unique URL that represents the location for the CIDR collection.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateCidrCollectionResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "collection" in value:
        import aws_sdk_route_53.types.cidr_collection

        aws_sdk_route_53.types.cidr_collection.serialize_xml(
            value["collection"], el, "Collection"
        )


def deserialize_xml(el: Element) -> CreateCidrCollectionResponse:
    out: CreateCidrCollectionResponse = {}  # type: ignore[typeddict-item]
    child_collection = el.find("Collection")
    if child_collection is not None:
        import aws_sdk_route_53.types.cidr_collection

        out["collection"] = aws_sdk_route_53.types.cidr_collection.deserialize_xml(
            child_collection
        )
    return out
