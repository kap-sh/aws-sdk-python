"""Generated from Smithy shape ``com.amazonaws.ec2#DeregisterInstanceEventNotificationAttributesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_tag_notification_attribute


class DeregisterInstanceEventNotificationAttributesResult(TypedDict, closed=True):
    instance_tag_attribute: NotRequired[
        "aws_sdk_ec2.types.instance_tag_notification_attribute.InstanceTagNotificationAttribute"
    ]
    """<p>The resulting set of tag keys.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeregisterInstanceEventNotificationAttributesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "instance_tag_attribute" in value:
        import aws_sdk_ec2.types.instance_tag_notification_attribute

        aws_sdk_ec2.types.instance_tag_notification_attribute.serialize_ec2_query(
            value["instance_tag_attribute"], pairs, f"{prefix}.InstanceTagAttribute"
        )


def deserialize_ec2_query(
    el: Element,
) -> DeregisterInstanceEventNotificationAttributesResult:
    out: DeregisterInstanceEventNotificationAttributesResult = {}  # type: ignore[typeddict-item]
    child_instance_tag_attribute = el.find("InstanceTagAttribute")
    if child_instance_tag_attribute is not None:
        import aws_sdk_ec2.types.instance_tag_notification_attribute

        out["instance_tag_attribute"] = (
            aws_sdk_ec2.types.instance_tag_notification_attribute.deserialize_ec2_query(
                child_instance_tag_attribute
            )
        )
    return out
