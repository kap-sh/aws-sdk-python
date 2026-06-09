"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceAttributeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_attribute_name
    import aws_sdk_ec2.types.instance_id


class DescribeInstanceAttributeRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance.</p>"""
    attribute: NotRequired[
        "aws_sdk_ec2.types.instance_attribute_name.InstanceAttributeName"
    ]
    """<p>The instance attribute.</p> <p>Note that the <code>enaSupport</code> attribute is not supported.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeInstanceAttributeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))
    if "attribute" in value:
        import aws_sdk_ec2.types.instance_attribute_name

        aws_sdk_ec2.types.instance_attribute_name.serialize_ec2_query(
            value["attribute"], pairs, f"{prefix}.Attribute"
        )


def deserialize_ec2_query(el: Element) -> DescribeInstanceAttributeRequest:
    out: DescribeInstanceAttributeRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_attribute = el.find("Attribute")
    if child_attribute is not None:
        import aws_sdk_ec2.types.instance_attribute_name

        out["attribute"] = (
            aws_sdk_ec2.types.instance_attribute_name.deserialize_ec2_query(
                child_attribute
            )
        )
    return out
