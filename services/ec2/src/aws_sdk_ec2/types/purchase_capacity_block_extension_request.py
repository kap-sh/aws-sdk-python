"""Generated from Smithy shape ``com.amazonaws.ec2#PurchaseCapacityBlockExtensionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.capacity_reservation_id
    import aws_sdk_ec2.types.offering_id


class PurchaseCapacityBlockExtensionRequest(TypedDict):
    capacity_block_extension_offering_id: NotRequired[
        "aws_sdk_ec2.types.offering_id.OfferingId"
    ]
    """<p>The ID of the Capacity Block extension offering to purchase.</p>"""
    capacity_reservation_id: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_id.CapacityReservationId"
    ]
    """<p>The ID of the Capacity reservation to be extended.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PurchaseCapacityBlockExtensionRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "capacity_block_extension_offering_id" in value:
        pairs.append(
            (
                f"{prefix}.CapacityBlockExtensionOfferingId",
                str(value["capacity_block_extension_offering_id"]),
            )
        )
    if "capacity_reservation_id" in value:
        pairs.append(
            (f"{prefix}.CapacityReservationId", str(value["capacity_reservation_id"]))
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> PurchaseCapacityBlockExtensionRequest:
    out: PurchaseCapacityBlockExtensionRequest = {}  # type: ignore[typeddict-item]
    child_capacity_block_extension_offering_id = el.find(
        "CapacityBlockExtensionOfferingId"
    )
    if child_capacity_block_extension_offering_id is not None:
        out["capacity_block_extension_offering_id"] = str(
            child_capacity_block_extension_offering_id.text or ""
        )
    child_capacity_reservation_id = el.find("CapacityReservationId")
    if child_capacity_reservation_id is not None:
        out["capacity_reservation_id"] = str(child_capacity_reservation_id.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
