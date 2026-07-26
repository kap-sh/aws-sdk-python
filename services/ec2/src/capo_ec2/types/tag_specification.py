"""Generated from Smithy shape ``com.amazonaws.ec2#TagSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.resource_type
    import capo_ec2.types.tag_list


class TagSpecification(TypedDict, closed=True):
    resource_type: NotRequired["capo_ec2.types.resource_type.ResourceType"]
    """<p>The type of resource to tag on creation.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags to apply to the resource.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TagSpecification, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_type" in value:
        import capo_ec2.types.resource_type

        capo_ec2.types.resource_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{prefix}.ResourceType"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_ec2_query(el: Element) -> TagSpecification:
    out: TagSpecification = {}  # type: ignore[typeddict-item]
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        import capo_ec2.types.resource_type

        out["resource_type"] = capo_ec2.types.resource_type.deserialize_ec2_query(
            child_resource_type
        )
    if el.find("Tags") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "Tags")
    return out
