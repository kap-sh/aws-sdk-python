"""Generated from Smithy shape ``com.amazonaws.ec2#ResetAddressAttributeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.address_attribute_name
    import aws_sdk_ec2.types.allocation_id
    import aws_sdk_ec2.types.boolean


class ResetAddressAttributeRequest(TypedDict):
    allocation_id: NotRequired["aws_sdk_ec2.types.allocation_id.AllocationId"]
    """<p>[EC2-VPC] The allocation ID.</p>"""
    attribute: NotRequired[
        "aws_sdk_ec2.types.address_attribute_name.AddressAttributeName"
    ]
    """<p>The attribute of the IP address.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ResetAddressAttributeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "allocation_id" in value:
        pairs.append((f"{prefix}.AllocationId", str(value["allocation_id"])))
    if "attribute" in value:
        import aws_sdk_ec2.types.address_attribute_name

        aws_sdk_ec2.types.address_attribute_name.serialize_ec2_query(
            value["attribute"], pairs, f"{prefix}.Attribute"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> ResetAddressAttributeRequest:
    out: ResetAddressAttributeRequest = {}  # type: ignore[typeddict-item]
    child_allocation_id = el.find("AllocationId")
    if child_allocation_id is not None:
        out["allocation_id"] = str(child_allocation_id.text or "")
    child_attribute = el.find("Attribute")
    if child_attribute is not None:
        import aws_sdk_ec2.types.address_attribute_name

        out["attribute"] = (
            aws_sdk_ec2.types.address_attribute_name.deserialize_ec2_query(
                child_attribute
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
