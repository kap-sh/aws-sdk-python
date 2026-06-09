"""Generated from Smithy shape ``com.amazonaws.ec2#DeregisterInstanceEventNotificationAttributesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.deregister_instance_tag_attribute_request


class DeregisterInstanceEventNotificationAttributesRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_tag_attribute: NotRequired[
        "aws_sdk_ec2.types.deregister_instance_tag_attribute_request.DeregisterInstanceTagAttributeRequest"
    ]
    """<p>Information about the tag keys to deregister.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeregisterInstanceEventNotificationAttributesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "instance_tag_attribute" in value:
        import aws_sdk_ec2.types.deregister_instance_tag_attribute_request

        aws_sdk_ec2.types.deregister_instance_tag_attribute_request.serialize_ec2_query(
            value["instance_tag_attribute"], pairs, f"{prefix}.InstanceTagAttribute"
        )


def deserialize_ec2_query(
    el: Element,
) -> DeregisterInstanceEventNotificationAttributesRequest:
    out: DeregisterInstanceEventNotificationAttributesRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_instance_tag_attribute = el.find("InstanceTagAttribute")
    if child_instance_tag_attribute is not None:
        import aws_sdk_ec2.types.deregister_instance_tag_attribute_request

        out["instance_tag_attribute"] = (
            aws_sdk_ec2.types.deregister_instance_tag_attribute_request.deserialize_ec2_query(
                child_instance_tag_attribute
            )
        )
    return out
