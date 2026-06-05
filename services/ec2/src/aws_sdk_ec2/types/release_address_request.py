"""Generated from Smithy shape ``com.amazonaws.ec2#ReleaseAddressRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.allocation_id
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class ReleaseAddressRequest(TypedDict):
    allocation_id: NotRequired["aws_sdk_ec2.types.allocation_id.AllocationId"]
    """<p>The allocation ID. This parameter is required.</p>"""
    public_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Deprecated.</p>"""
    network_border_group: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The set of Availability Zones, Local Zones, or Wavelength Zones from which Amazon Web Services advertises IP addresses.</p> <p>If you provide an incorrect network border group, you receive an <code>InvalidAddress.NotFound</code> error.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReleaseAddressRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "allocation_id" in value:
        pairs.append((f"{prefix}.AllocationId", str(value["allocation_id"])))
    if "public_ip" in value:
        pairs.append((f"{prefix}.PublicIp", str(value["public_ip"])))
    if "network_border_group" in value:
        pairs.append(
            (f"{prefix}.NetworkBorderGroup", str(value["network_border_group"]))
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> ReleaseAddressRequest:
    out: ReleaseAddressRequest = {}  # type: ignore[typeddict-item]
    child_allocation_id = el.find("AllocationId")
    if child_allocation_id is not None:
        out["allocation_id"] = str(child_allocation_id.text or "")
    child_public_ip = el.find("PublicIp")
    if child_public_ip is not None:
        out["public_ip"] = str(child_public_ip.text or "")
    child_network_border_group = el.find("NetworkBorderGroup")
    if child_network_border_group is not None:
        out["network_border_group"] = str(child_network_border_group.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
