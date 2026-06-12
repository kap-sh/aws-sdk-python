"""Generated from Smithy shape ``com.amazonaws.route53#DeleteCidrCollectionResponse``."""

from typing import TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement


class DeleteCidrCollectionResponse(TypedDict):
    pass


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteCidrCollectionResponse, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteCidrCollectionResponse:
    out: DeleteCidrCollectionResponse = {}  # type: ignore[typeddict-item]
    return out
