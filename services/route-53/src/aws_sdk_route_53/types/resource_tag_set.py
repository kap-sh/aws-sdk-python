"""Generated from Smithy shape ``com.amazonaws.route53#ResourceTagSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.tag_list
    import aws_sdk_route_53.types.tag_resource_id
    import aws_sdk_route_53.types.tag_resource_type


class ResourceTagSet(TypedDict, closed=True):
    resource_type: NotRequired[
        "aws_sdk_route_53.types.tag_resource_type.TagResourceType"
    ]
    """<p>The type of the resource.</p> <ul> <li> <p>The resource type for health checks is <code>healthcheck</code>.</p> </li> <li> <p>The resource type for hosted zones is <code>hostedzone</code>.</p> </li> </ul>"""
    resource_id: NotRequired["aws_sdk_route_53.types.tag_resource_id.TagResourceId"]
    """<p>The ID for the specified resource.</p>"""
    tags: NotRequired["aws_sdk_route_53.types.tag_list.TagList"]
    """<p>The tags associated with the specified resource.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ResourceTagSet, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "resource_type" in value:
        import aws_sdk_route_53.types.tag_resource_type

        aws_sdk_route_53.types.tag_resource_type.serialize_xml(
            value["resource_type"], el, "ResourceType"
        )
    if "resource_id" in value:
        SubElement(el, "ResourceId").text = str(value["resource_id"])
    if "tags" in value:
        import aws_sdk_route_53.types.tag_list

        aws_sdk_route_53.types.tag_list.serialize_xml(value["tags"], el, "Tags")


def deserialize_xml(el: Element) -> ResourceTagSet:
    out: ResourceTagSet = {}  # type: ignore[typeddict-item]
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        import aws_sdk_route_53.types.tag_resource_type

        out["resource_type"] = aws_sdk_route_53.types.tag_resource_type.deserialize_xml(
            child_resource_type
        )
    child_resource_id = el.find("ResourceId")
    if child_resource_id is not None:
        out["resource_id"] = str(child_resource_id.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_route_53.types.tag_list

        out["tags"] = aws_sdk_route_53.types.tag_list.deserialize_xml(child_tags)
    return out
