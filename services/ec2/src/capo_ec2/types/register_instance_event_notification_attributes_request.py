"""Generated from Smithy shape ``com.amazonaws.ec2#RegisterInstanceEventNotificationAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.register_instance_tag_attribute_request


class RegisterInstanceEventNotificationAttributesRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_tag_attribute: NotRequired[
        "capo_ec2.types.register_instance_tag_attribute_request.RegisterInstanceTagAttributeRequest"
    ]
    """<p>Information about the tag keys to register.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RegisterInstanceEventNotificationAttributesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "instance_tag_attribute" in value:
        import capo_ec2.types.register_instance_tag_attribute_request

        capo_ec2.types.register_instance_tag_attribute_request.serialize_ec2_query(
            value["instance_tag_attribute"], pairs, f"{key_prefix}InstanceTagAttribute"
        )


def deserialize_ec2_query(
    el: Element,
) -> RegisterInstanceEventNotificationAttributesRequest:
    out: RegisterInstanceEventNotificationAttributesRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_instance_tag_attribute = el.find("InstanceTagAttribute")
    if child_instance_tag_attribute is not None:
        import capo_ec2.types.register_instance_tag_attribute_request

        out["instance_tag_attribute"] = (
            capo_ec2.types.register_instance_tag_attribute_request.deserialize_ec2_query(
                child_instance_tag_attribute
            )
        )
    return out
