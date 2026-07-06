"""Generated from Smithy shape ``com.amazonaws.autoscaling#TagDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.propagate_at_launch
    import aws_sdk_auto_scaling.types.tag_key
    import aws_sdk_auto_scaling.types.tag_value
    import aws_sdk_auto_scaling.types.xml_string


class TagDescription(TypedDict, closed=True):
    resource_id: NotRequired["aws_sdk_auto_scaling.types.xml_string.XmlString"]
    """<p>The name of the group.</p>"""
    resource_type: NotRequired["aws_sdk_auto_scaling.types.xml_string.XmlString"]
    """<p>The type of resource. The only supported value is <code>auto-scaling-group</code>.</p>"""
    key: NotRequired["aws_sdk_auto_scaling.types.tag_key.TagKey"]
    """<p>The tag key.</p>"""
    value: NotRequired["aws_sdk_auto_scaling.types.tag_value.TagValue"]
    """<p>The tag value.</p>"""
    propagate_at_launch: NotRequired[
        "aws_sdk_auto_scaling.types.propagate_at_launch.PropagateAtLaunch"
    ]
    """<p>Determines whether the tag is added to new instances as they are launched in the group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TagDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_id" in value:
        pairs.append((f"{prefix}.ResourceId", str(value["resource_id"])))
    if "resource_type" in value:
        pairs.append((f"{prefix}.ResourceType", str(value["resource_type"])))
    if "key" in value:
        pairs.append((f"{prefix}.Key", str(value["key"])))
    if "value" in value:
        pairs.append((f"{prefix}.Value", str(value["value"])))
    if "propagate_at_launch" in value:
        pairs.append(
            (
                f"{prefix}.PropagateAtLaunch",
                "true" if value["propagate_at_launch"] else "false",
            )
        )


def deserialize_query(el: Element) -> TagDescription:
    out: TagDescription = {}  # type: ignore[typeddict-item]
    child_resource_id = el.find("ResourceId")
    if child_resource_id is not None:
        out["resource_id"] = str(child_resource_id.text or "")
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        out["resource_type"] = str(child_resource_type.text or "")
    child_key = el.find("Key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    child_propagate_at_launch = el.find("PropagateAtLaunch")
    if child_propagate_at_launch is not None:
        out["propagate_at_launch"] = (
            child_propagate_at_launch.text or ""
        ).lower() == "true"
    return out
