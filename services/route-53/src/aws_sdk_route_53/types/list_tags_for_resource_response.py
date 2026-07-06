"""Generated from Smithy shape ``com.amazonaws.route53#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.resource_tag_set


class ListTagsForResourceResponse(TypedDict, closed=True):
    resource_tag_set: "aws_sdk_route_53.types.resource_tag_set.ResourceTagSet"
    """<p>A <code>ResourceTagSet</code> containing tags associated with the specified resource.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListTagsForResourceResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_route_53.types.resource_tag_set

    aws_sdk_route_53.types.resource_tag_set.serialize_xml(
        value["resource_tag_set"], el, "ResourceTagSet"
    )


def deserialize_xml(el: Element) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    child_resource_tag_set = el.find("ResourceTagSet")
    if child_resource_tag_set is not None:
        import aws_sdk_route_53.types.resource_tag_set

        out["resource_tag_set"] = (
            aws_sdk_route_53.types.resource_tag_set.deserialize_xml(
                child_resource_tag_set
            )
        )
    else:
        raise DeserializationError(
            "ListTagsForResourceResponse.resource_tag_set required"
        )
    return out
