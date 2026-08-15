"""Generated from Smithy shape ``com.amazonaws.ec2#CancellationTerms``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.apply_cancellation_charges
    import capo_ec2.types.boxed_integer
    import capo_ec2.types.boxed_long
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string


class CancellationTerms(TypedDict, closed=True):
    cancellation_type: NotRequired[
        "capo_ec2.types.apply_cancellation_charges.ApplyCancellationCharges"
    ]
    """<p>The type of cancellation charge. Possible values include <code>commitment-wind-down</code>.</p>"""
    reservation_state: NotRequired["capo_ec2.types.string.String"]
    """<p>The state that the Capacity Reservation will transition to after cancellation.</p>"""
    committed_instance_count: NotRequired["capo_ec2.types.boxed_integer.BoxedInteger"]
    """<p>The number of instances under commitment after cancellation.</p>"""
    charge_commitment_duration_hours: NotRequired["capo_ec2.types.boxed_long.BoxedLong"]
    """<p>The number of hours for which cancellation charges will apply.</p>"""
    charge_end_date: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time at which cancellation charges will stop.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CancellationTerms, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cancellation_type" in value:
        import capo_ec2.types.apply_cancellation_charges

        capo_ec2.types.apply_cancellation_charges.serialize_ec2_query(
            value["cancellation_type"], pairs, f"{key_prefix}CancellationType"
        )
    if "reservation_state" in value:
        pairs.append((f"{key_prefix}ReservationState", str(value["reservation_state"])))
    if "committed_instance_count" in value:
        pairs.append(
            (
                f"{key_prefix}CommittedInstanceCount",
                str(value["committed_instance_count"]),
            )
        )
    if "charge_commitment_duration_hours" in value:
        pairs.append(
            (
                f"{key_prefix}ChargeCommitmentDurationHours",
                str(value["charge_commitment_duration_hours"]),
            )
        )
    if "charge_end_date" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["charge_end_date"], pairs, f"{key_prefix}ChargeEndDate"
        )


def deserialize_ec2_query(el: Element) -> CancellationTerms:
    out: CancellationTerms = {}  # type: ignore[typeddict-item]
    child_cancellation_type = el.find("cancellationType")
    if child_cancellation_type is not None:
        import capo_ec2.types.apply_cancellation_charges

        out["cancellation_type"] = (
            capo_ec2.types.apply_cancellation_charges.deserialize_ec2_query(
                child_cancellation_type
            )
        )
    child_reservation_state = el.find("reservationState")
    if child_reservation_state is not None:
        out["reservation_state"] = str(child_reservation_state.text or "")
    child_committed_instance_count = el.find("committedInstanceCount")
    if child_committed_instance_count is not None:
        out["committed_instance_count"] = int(child_committed_instance_count.text or "")
    child_charge_commitment_duration_hours = el.find("chargeCommitmentDurationHours")
    if child_charge_commitment_duration_hours is not None:
        out["charge_commitment_duration_hours"] = int(
            child_charge_commitment_duration_hours.text or ""
        )
    child_charge_end_date = el.find("chargeEndDate")
    if child_charge_end_date is not None:
        import capo_ec2.types.millisecond_date_time

        out["charge_end_date"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_charge_end_date
            )
        )
    return out
