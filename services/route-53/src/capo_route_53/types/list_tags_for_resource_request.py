"""Generated from Smithy shape ``com.amazonaws.route53#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.tag_resource_id
    import capo_route_53.types.tag_resource_type


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_type: "capo_route_53.types.tag_resource_type.TagResourceType"
    """<p>The type of the resource.</p> <ul> <li> <p>The resource type for health checks is <code>healthcheck</code>.</p> </li> <li> <p>The resource type for hosted zones is <code>hostedzone</code>.</p> </li> </ul>"""
    resource_id: "capo_route_53.types.tag_resource_id.TagResourceId"
    """<p>The ID of the resource for which you want to retrieve tags.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListTagsForResourceRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
