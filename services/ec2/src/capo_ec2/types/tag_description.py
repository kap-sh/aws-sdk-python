"""Generated from Smithy shape ``com.amazonaws.ec2#TagDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.resource_type
    import capo_ec2.types.string


class TagDescription(TypedDict, closed=True):
    key: NotRequired["capo_ec2.types.string.String"]
    """<p>The tag key.</p>"""
    resource_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the resource.</p>"""
    resource_type: NotRequired["capo_ec2.types.resource_type.ResourceType"]
    """<p>The resource type.</p>"""
    value: NotRequired["capo_ec2.types.string.String"]
    """<p>The tag value.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TagDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "key" in value:
        pairs.append((f"{key_prefix}Key", str(value["key"])))
    if "resource_id" in value:
        pairs.append((f"{key_prefix}ResourceId", str(value["resource_id"])))
    if "resource_type" in value:
        import capo_ec2.types.resource_type

        capo_ec2.types.resource_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{key_prefix}ResourceType"
        )
    if "value" in value:
        pairs.append((f"{key_prefix}Value", str(value["value"])))


def deserialize_ec2_query(el: Element) -> TagDescription:
    out: TagDescription = {}  # type: ignore[typeddict-item]
    child_key = el.find("Key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    child_resource_id = el.find("ResourceId")
    if child_resource_id is not None:
        out["resource_id"] = str(child_resource_id.text or "")
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        import capo_ec2.types.resource_type

        out["resource_type"] = capo_ec2.types.resource_type.deserialize_ec2_query(
            child_resource_type
        )
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    return out
