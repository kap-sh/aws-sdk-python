"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyCapacityReservationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.capacity_reservation_id
    import capo_ec2.types.date_time
    import capo_ec2.types.end_date_type
    import capo_ec2.types.instance_match_criteria
    import capo_ec2.types.integer
    import capo_ec2.types.string


class ModifyCapacityReservationRequest(TypedDict, closed=True):
    capacity_reservation_id: NotRequired[
        "capo_ec2.types.capacity_reservation_id.CapacityReservationId"
    ]
    """<p>The ID of the Capacity Reservation.</p>"""
    instance_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of instances for which to reserve capacity. The number of instances can't be increased or decreased by more than <code>1000</code> in a single request.</p>"""
    end_date: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The date and time at which the Capacity Reservation expires. When a Capacity Reservation expires, the reserved capacity is released and you can no longer launch instances into it. The Capacity Reservation's state changes to <code>expired</code> when it reaches its end date and time.</p> <p>The Capacity Reservation is cancelled within an hour from the specified time. For example, if you specify 5/31/2019, 13:30:55, the Capacity Reservation is guaranteed to end between 13:30:55 and 14:30:55 on 5/31/2019.</p> <p>You must provide an <code>EndDate</code> value if <code>EndDateType</code> is <code>limited</code>. Omit <code>EndDate</code> if <code>EndDateType</code> is <code>unlimited</code>.</p>"""
    end_date_type: NotRequired["capo_ec2.types.end_date_type.EndDateType"]
    """<p>Indicates the way in which the Capacity Reservation ends. A Capacity Reservation can have one of the following end types:</p> <ul> <li> <p> <code>unlimited</code> - The Capacity Reservation remains active until you explicitly cancel it. Do not provide an <code>EndDate</code> value if <code>EndDateType</code> is <code>unlimited</code>.</p> </li> <li> <p> <code>limited</code> - The Capacity Reservation expires automatically at a specified date and time. You must provide an <code>EndDate</code> value if <code>EndDateType</code> is <code>limited</code>.</p> </li> </ul>"""
    accept: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Reserved. Capacity Reservations you have created are accepted by default.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    additional_info: NotRequired["capo_ec2.types.string.String"]
    """<p>Reserved for future use.</p>"""
    instance_match_criteria: NotRequired[
        "capo_ec2.types.instance_match_criteria.InstanceMatchCriteria"
    ]
    """<p> The matching criteria (instance eligibility) that you want to use in the modified Capacity Reservation. If you change the instance eligibility of an existing Capacity Reservation from <code>targeted</code> to <code>open</code>, any running instances that match the attributes of the Capacity Reservation, have the <code>CapacityReservationPreference</code> set to <code>open</code>, and are not yet running in the Capacity Reservation, will automatically use the modified Capacity Reservation. </p> <p>To modify the instance eligibility, the Capacity Reservation must be completely idle (zero usage).</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyCapacityReservationRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "capacity_reservation_id" in value:
        pairs.append(
            (f"{prefix}.CapacityReservationId", str(value["capacity_reservation_id"]))
        )
    if "instance_count" in value:
        pairs.append((f"{prefix}.InstanceCount", str(value["instance_count"])))
    if "end_date" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["end_date"], pairs, f"{prefix}.EndDate"
        )
    if "end_date_type" in value:
        import capo_ec2.types.end_date_type

        capo_ec2.types.end_date_type.serialize_ec2_query(
            value["end_date_type"], pairs, f"{prefix}.EndDateType"
        )
    if "accept" in value:
        pairs.append((f"{prefix}.Accept", "true" if value["accept"] else "false"))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "additional_info" in value:
        pairs.append((f"{prefix}.AdditionalInfo", str(value["additional_info"])))
    if "instance_match_criteria" in value:
        import capo_ec2.types.instance_match_criteria

        capo_ec2.types.instance_match_criteria.serialize_ec2_query(
            value["instance_match_criteria"], pairs, f"{prefix}.InstanceMatchCriteria"
        )


def deserialize_ec2_query(el: Element) -> ModifyCapacityReservationRequest:
    out: ModifyCapacityReservationRequest = {}  # type: ignore[typeddict-item]
    child_capacity_reservation_id = el.find("CapacityReservationId")
    if child_capacity_reservation_id is not None:
        out["capacity_reservation_id"] = str(child_capacity_reservation_id.text or "")
    child_instance_count = el.find("InstanceCount")
    if child_instance_count is not None:
        out["instance_count"] = int(child_instance_count.text or "")
    child_end_date = el.find("EndDate")
    if child_end_date is not None:
        import capo_ec2.types.date_time

        out["end_date"] = capo_ec2.types.date_time.deserialize_ec2_query(child_end_date)
    child_end_date_type = el.find("EndDateType")
    if child_end_date_type is not None:
        import capo_ec2.types.end_date_type

        out["end_date_type"] = capo_ec2.types.end_date_type.deserialize_ec2_query(
            child_end_date_type
        )
    child_accept = el.find("Accept")
    if child_accept is not None:
        out["accept"] = (child_accept.text or "").lower() == "true"
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_additional_info = el.find("AdditionalInfo")
    if child_additional_info is not None:
        out["additional_info"] = str(child_additional_info.text or "")
    child_instance_match_criteria = el.find("InstanceMatchCriteria")
    if child_instance_match_criteria is not None:
        import capo_ec2.types.instance_match_criteria

        out["instance_match_criteria"] = (
            capo_ec2.types.instance_match_criteria.deserialize_ec2_query(
                child_instance_match_criteria
            )
        )
    return out
