"""Generated from Smithy shape ``com.amazonaws.cloudfront#DeleteConnectionFunctionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.resource_id
    import capo_cloudfront.types.string


class DeleteConnectionFunctionRequest(TypedDict, closed=True):
    id: "capo_cloudfront.types.resource_id.ResourceId"
    """<p>The connection function's ID.</p>"""
    if_match: "capo_cloudfront.types.string.string"
    """<p>The current version (<code>ETag</code> value) of the connection function you are deleting.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteConnectionFunctionRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteConnectionFunctionRequest:
    out: DeleteConnectionFunctionRequest = {}  # type: ignore[typeddict-item]
    return out
