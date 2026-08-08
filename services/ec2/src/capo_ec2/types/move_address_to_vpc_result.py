"""Generated from Smithy shape ``com.amazonaws.ec2#MoveAddressToVpcResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.status
    import capo_ec2.types.string


class MoveAddressToVpcResult(TypedDict, closed=True):
    allocation_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The allocation ID for the Elastic IP address.</p>"""
    status: NotRequired["capo_ec2.types.status.Status"]
    """<p>The status of the move of the IP address.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: MoveAddressToVpcResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "allocation_id" in value:
        pairs.append((f"{key_prefix}AllocationId", str(value["allocation_id"])))
    if "status" in value:
        import capo_ec2.types.status

        capo_ec2.types.status.serialize_ec2_query(
            value["status"], pairs, f"{key_prefix}Status"
        )


def deserialize_ec2_query(el: Element) -> MoveAddressToVpcResult:
    out: MoveAddressToVpcResult = {}  # type: ignore[typeddict-item]
    child_allocation_id = el.find("allocationId")
    if child_allocation_id is not None:
        out["allocation_id"] = str(child_allocation_id.text or "")
    child_status = el.find("status")
    if child_status is not None:
        import capo_ec2.types.status

        out["status"] = capo_ec2.types.status.deserialize_ec2_query(child_status)
    return out
