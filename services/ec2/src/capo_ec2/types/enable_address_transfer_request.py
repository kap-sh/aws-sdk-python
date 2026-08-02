"""Generated from Smithy shape ``com.amazonaws.ec2#EnableAddressTransferRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.allocation_id
    import capo_ec2.types.boolean
    import capo_ec2.types.string


class EnableAddressTransferRequest(TypedDict, closed=True):
    allocation_id: NotRequired["capo_ec2.types.allocation_id.AllocationId"]
    """<p>The allocation ID of an Elastic IP address.</p>"""
    transfer_account_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the account that you want to transfer the Elastic IP address to.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableAddressTransferRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "allocation_id" in value:
        pairs.append((f"{key_prefix}AllocationId", str(value["allocation_id"])))
    if "transfer_account_id" in value:
        pairs.append(
            (f"{key_prefix}TransferAccountId", str(value["transfer_account_id"]))
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> EnableAddressTransferRequest:
    out: EnableAddressTransferRequest = {}  # type: ignore[typeddict-item]
    child_allocation_id = el.find("AllocationId")
    if child_allocation_id is not None:
        out["allocation_id"] = str(child_allocation_id.text or "")
    child_transfer_account_id = el.find("TransferAccountId")
    if child_transfer_account_id is not None:
        out["transfer_account_id"] = str(child_transfer_account_id.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
