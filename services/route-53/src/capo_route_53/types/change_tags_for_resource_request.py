"""Generated from Smithy shape ``com.amazonaws.route53#ChangeTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.tag_key_list
    import capo_route_53.types.tag_list
    import capo_route_53.types.tag_resource_id
    import capo_route_53.types.tag_resource_type


class ChangeTagsForResourceRequest(TypedDict, closed=True):
    resource_type: "capo_route_53.types.tag_resource_type.TagResourceType"
    """<p>The type of the resource.</p> <ul> <li> <p>The resource type for health checks is <code>healthcheck</code>.</p> </li> <li> <p>The resource type for hosted zones is <code>hostedzone</code>.</p> </li> </ul>"""
    resource_id: "capo_route_53.types.tag_resource_id.TagResourceId"
    """<p>The ID of the resource for which you want to add, change, or delete tags.</p>"""
    add_tags: NotRequired["capo_route_53.types.tag_list.TagList"]
    """<p>A complex type that contains a list of the tags that you want to add to the specified health check or hosted zone and/or the tags that you want to edit <code>Value</code> for.</p> <p>You can add a maximum of 10 tags to a health check or a hosted zone.</p>"""
    remove_tag_keys: NotRequired["capo_route_53.types.tag_key_list.TagKeyList"]
    """<p>A complex type that contains a list of the tags that you want to delete from the specified health check or hosted zone. You can specify up to 10 keys.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ChangeTagsForResourceRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "add_tags" in value:
        import capo_route_53.types.tag_list

        capo_route_53.types.tag_list.serialize_xml(value["add_tags"], el, "AddTags")
    if "remove_tag_keys" in value:
        import capo_route_53.types.tag_key_list

        capo_route_53.types.tag_key_list.serialize_xml(
            value["remove_tag_keys"], el, "RemoveTagKeys"
        )


def deserialize_xml(el: Element) -> ChangeTagsForResourceRequest:
    out: ChangeTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    child_add_tags = el.find("AddTags")
    if child_add_tags is not None:
        import capo_route_53.types.tag_list

        out["add_tags"] = capo_route_53.types.tag_list.deserialize_xml(child_add_tags)
    child_remove_tag_keys = el.find("RemoveTagKeys")
    if child_remove_tag_keys is not None:
        import capo_route_53.types.tag_key_list

        out["remove_tag_keys"] = capo_route_53.types.tag_key_list.deserialize_xml(
            child_remove_tag_keys
        )
    return out
