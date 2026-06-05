"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcAttributeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.vpc_attribute_name
    import aws_sdk_ec2.types.vpc_id


class DescribeVpcAttributeRequest(TypedDict):
    attribute: NotRequired["aws_sdk_ec2.types.vpc_attribute_name.VpcAttributeName"]
    """<p>The VPC attribute.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcAttributeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "attribute" in value:
        import aws_sdk_ec2.types.vpc_attribute_name

        aws_sdk_ec2.types.vpc_attribute_name.serialize_ec2_query(
            value["attribute"], pairs, f"{prefix}.Attribute"
        )
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DescribeVpcAttributeRequest:
    out: DescribeVpcAttributeRequest = {}  # type: ignore[typeddict-item]
    child_attribute = el.find("Attribute")
    if child_attribute is not None:
        import aws_sdk_ec2.types.vpc_attribute_name

        out["attribute"] = aws_sdk_ec2.types.vpc_attribute_name.deserialize_ec2_query(
            child_attribute
        )
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
