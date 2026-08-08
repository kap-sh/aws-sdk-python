"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceEventNotificationAttributesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_tag_notification_attribute


class DescribeInstanceEventNotificationAttributesResult(TypedDict, closed=True):
    instance_tag_attribute: NotRequired[
        "capo_ec2.types.instance_tag_notification_attribute.InstanceTagNotificationAttribute"
    ]
    """<p>Information about the registered tag keys.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeInstanceEventNotificationAttributesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_tag_attribute" in value:
        import capo_ec2.types.instance_tag_notification_attribute

        capo_ec2.types.instance_tag_notification_attribute.serialize_ec2_query(
            value["instance_tag_attribute"], pairs, f"{key_prefix}InstanceTagAttribute"
        )


def deserialize_ec2_query(
    el: Element,
) -> DescribeInstanceEventNotificationAttributesResult:
    out: DescribeInstanceEventNotificationAttributesResult = {}  # type: ignore[typeddict-item]
    child_instance_tag_attribute = el.find("instanceTagAttribute")
    if child_instance_tag_attribute is not None:
        import capo_ec2.types.instance_tag_notification_attribute

        out["instance_tag_attribute"] = (
            capo_ec2.types.instance_tag_notification_attribute.deserialize_ec2_query(
                child_instance_tag_attribute
            )
        )
    return out
