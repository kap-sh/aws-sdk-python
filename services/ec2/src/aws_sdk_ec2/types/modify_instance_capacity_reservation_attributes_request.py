"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceCapacityReservationAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.capacity_reservation_specification
    import aws_sdk_ec2.types.instance_id


class ModifyInstanceCapacityReservationAttributesRequest(TypedDict, closed=True):
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance to be modified.</p>"""
    capacity_reservation_specification: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_specification.CapacityReservationSpecification"
    ]
    """<p>Information about the Capacity Reservation targeting option.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyInstanceCapacityReservationAttributesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))
    if "capacity_reservation_specification" in value:
        import aws_sdk_ec2.types.capacity_reservation_specification

        aws_sdk_ec2.types.capacity_reservation_specification.serialize_ec2_query(
            value["capacity_reservation_specification"],
            pairs,
            f"{prefix}.CapacityReservationSpecification",
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> ModifyInstanceCapacityReservationAttributesRequest:
    out: ModifyInstanceCapacityReservationAttributesRequest = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_capacity_reservation_specification = el.find(
        "CapacityReservationSpecification"
    )
    if child_capacity_reservation_specification is not None:
        import aws_sdk_ec2.types.capacity_reservation_specification

        out["capacity_reservation_specification"] = (
            aws_sdk_ec2.types.capacity_reservation_specification.deserialize_ec2_query(
                child_capacity_reservation_specification
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
