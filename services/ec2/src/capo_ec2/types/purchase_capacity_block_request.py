"""Generated from Smithy shape ``com.amazonaws.ec2#PurchaseCapacityBlockRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.capacity_reservation_instance_platform
    import capo_ec2.types.offering_id
    import capo_ec2.types.tag_specification_list


class PurchaseCapacityBlockRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the Capacity Block during launch.</p>"""
    capacity_block_offering_id: NotRequired["capo_ec2.types.offering_id.OfferingId"]
    """<p>The ID of the Capacity Block offering.</p>"""
    instance_platform: NotRequired[
        "capo_ec2.types.capacity_reservation_instance_platform.CapacityReservationInstancePlatform"
    ]
    """<p>The type of operating system for which to reserve capacity.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PurchaseCapacityBlockRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "capacity_block_offering_id" in value:
        pairs.append(
            (
                f"{key_prefix}CapacityBlockOfferingId",
                str(value["capacity_block_offering_id"]),
            )
        )
    if "instance_platform" in value:
        import capo_ec2.types.capacity_reservation_instance_platform

        capo_ec2.types.capacity_reservation_instance_platform.serialize_ec2_query(
            value["instance_platform"], pairs, f"{key_prefix}InstancePlatform"
        )


def deserialize_ec2_query(el: Element) -> PurchaseCapacityBlockRequest:
    out: PurchaseCapacityBlockRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_capacity_block_offering_id = el.find("CapacityBlockOfferingId")
    if child_capacity_block_offering_id is not None:
        out["capacity_block_offering_id"] = str(
            child_capacity_block_offering_id.text or ""
        )
    child_instance_platform = el.find("InstancePlatform")
    if child_instance_platform is not None:
        import capo_ec2.types.capacity_reservation_instance_platform

        out["instance_platform"] = (
            capo_ec2.types.capacity_reservation_instance_platform.deserialize_ec2_query(
                child_instance_platform
            )
        )
    return out
