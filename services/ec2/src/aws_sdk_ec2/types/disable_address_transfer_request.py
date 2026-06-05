"""Generated from Smithy shape ``com.amazonaws.ec2#DisableAddressTransferRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.allocation_id
    import aws_sdk_ec2.types.boolean


class DisableAddressTransferRequest(TypedDict):
    allocation_id: NotRequired["aws_sdk_ec2.types.allocation_id.AllocationId"]
    """<p>The allocation ID of an Elastic IP address.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisableAddressTransferRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "allocation_id" in value:
        pairs.append((f"{prefix}.AllocationId", str(value["allocation_id"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DisableAddressTransferRequest:
    out: DisableAddressTransferRequest = {}  # type: ignore[typeddict-item]
    child_allocation_id = el.find("AllocationId")
    if child_allocation_id is not None:
        out["allocation_id"] = str(child_allocation_id.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
