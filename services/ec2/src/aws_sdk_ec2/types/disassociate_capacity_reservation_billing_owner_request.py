"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateCapacityReservationBillingOwnerRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.account_id
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.capacity_reservation_id


class DisassociateCapacityReservationBillingOwnerRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    capacity_reservation_id: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_id.CapacityReservationId"
    ]
    """<p>The ID of the Capacity Reservation.</p>"""
    unused_reservation_billing_owner_id: NotRequired[
        "aws_sdk_ec2.types.account_id.AccountID"
    ]
    """<p>The ID of the consumer account to which the request was sent.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisassociateCapacityReservationBillingOwnerRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "capacity_reservation_id" in value:
        pairs.append(
            (f"{prefix}.CapacityReservationId", str(value["capacity_reservation_id"]))
        )
    if "unused_reservation_billing_owner_id" in value:
        pairs.append(
            (
                f"{prefix}.UnusedReservationBillingOwnerId",
                str(value["unused_reservation_billing_owner_id"]),
            )
        )


def deserialize_ec2_query(
    el: Element,
) -> DisassociateCapacityReservationBillingOwnerRequest:
    out: DisassociateCapacityReservationBillingOwnerRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_capacity_reservation_id = el.find("CapacityReservationId")
    if child_capacity_reservation_id is not None:
        out["capacity_reservation_id"] = str(child_capacity_reservation_id.text or "")
    child_unused_reservation_billing_owner_id = el.find(
        "UnusedReservationBillingOwnerId"
    )
    if child_unused_reservation_billing_owner_id is not None:
        out["unused_reservation_billing_owner_id"] = str(
            child_unused_reservation_billing_owner_id.text or ""
        )
    return out
