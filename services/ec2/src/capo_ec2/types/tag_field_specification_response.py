"""Generated from Smithy shape ``com.amazonaws.ec2#TagFieldSpecificationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.tag_key_list
    import capo_ec2.types.taggable_resource_type


class TagFieldSpecificationResponse(TypedDict, closed=True):
    resource_type: NotRequired[
        "capo_ec2.types.taggable_resource_type.TaggableResourceType"
    ]
    """<p>The resource type for the tag keys associated with the Flow Logs Amazon EC2 Tags feature fields in your custom log format.</p>"""
    tag_keys: NotRequired["capo_ec2.types.tag_key_list.TagKeyList"]
    """<p>The tag keys on your tagged resources to be displayed by the Flow Logs Amazon EC2 Tags feature fields in your custom log format.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TagFieldSpecificationResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resource_type" in value:
        import capo_ec2.types.taggable_resource_type

        capo_ec2.types.taggable_resource_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{key_prefix}ResourceType"
        )
    if "tag_keys" in value:
        import capo_ec2.types.tag_key_list

        capo_ec2.types.tag_key_list.serialize_ec2_query(
            value["tag_keys"], pairs, f"{key_prefix}TagKeySet"
        )


def deserialize_ec2_query(el: Element) -> TagFieldSpecificationResponse:
    out: TagFieldSpecificationResponse = {}  # type: ignore[typeddict-item]
    child_resource_type = el.find("resourceType")
    if child_resource_type is not None:
        import capo_ec2.types.taggable_resource_type

        out["resource_type"] = (
            capo_ec2.types.taggable_resource_type.deserialize_ec2_query(
                child_resource_type
            )
        )
    child_tag_keys = el.find("tagKeySet")
    if child_tag_keys is not None:
        import capo_ec2.types.tag_key_list

        out["tag_keys"] = capo_ec2.types.tag_key_list.deserialize_ec2_query(
            child_tag_keys
        )
    return out
