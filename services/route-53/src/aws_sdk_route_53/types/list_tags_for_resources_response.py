"""Generated from Smithy shape ``com.amazonaws.route53#ListTagsForResourcesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.resource_tag_set_list


class ListTagsForResourcesResponse(TypedDict):
    resource_tag_sets: "aws_sdk_route_53.types.resource_tag_set_list.ResourceTagSetList"
    """<p>A list of <code>ResourceTagSet</code>s containing tags associated with the specified resources.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListTagsForResourcesResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_route_53.types.resource_tag_set_list

    aws_sdk_route_53.types.resource_tag_set_list.serialize_xml(
        value["resource_tag_sets"], el, "ResourceTagSets"
    )


def deserialize_xml(el: Element) -> ListTagsForResourcesResponse:
    out: ListTagsForResourcesResponse = {}  # type: ignore[typeddict-item]
    child_resource_tag_sets = el.find("ResourceTagSets")
    if child_resource_tag_sets is not None:
        import aws_sdk_route_53.types.resource_tag_set_list

        out["resource_tag_sets"] = (
            aws_sdk_route_53.types.resource_tag_set_list.deserialize_xml(
                child_resource_tag_sets
            )
        )
    else:
        raise DeserializationError(
            "ListTagsForResourcesResponse.resource_tag_sets required"
        )
    return out
