"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceAttributeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.instance_attribute_name
    import capo_ec2.types.instance_id


class DescribeInstanceAttributeRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_id: NotRequired["capo_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance.</p>"""
    attribute: NotRequired[
        "capo_ec2.types.instance_attribute_name.InstanceAttributeName"
    ]
    """<p>The instance attribute.</p> <p>Note that the <code>enaSupport</code> attribute is not supported.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeInstanceAttributeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "attribute" in value:
        import capo_ec2.types.instance_attribute_name

        capo_ec2.types.instance_attribute_name.serialize_ec2_query(
            value["attribute"], pairs, f"{key_prefix}Attribute"
        )


def deserialize_ec2_query(el: Element) -> DescribeInstanceAttributeRequest:
    out: DescribeInstanceAttributeRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_instance_id = el.find("instanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_attribute = el.find("attribute")
    if child_attribute is not None:
        import capo_ec2.types.instance_attribute_name

        out["attribute"] = capo_ec2.types.instance_attribute_name.deserialize_ec2_query(
            child_attribute
        )
    return out
