"""Generated from Smithy shape ``com.amazonaws.route53#DeleteCidrCollectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.uuid


class DeleteCidrCollectionRequest(TypedDict, closed=True):
    id: "aws_sdk_route_53.types.uuid.UUID"
    """<p>The UUID of the collection to delete.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteCidrCollectionRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteCidrCollectionRequest:
    out: DeleteCidrCollectionRequest = {}  # type: ignore[typeddict-item]
    return out
