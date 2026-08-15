"""Generated from Smithy shape ``com.amazonaws.ec2#CancelCapacityReservationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.apply_cancellation_charges
    import capo_ec2.types.boolean
    import capo_ec2.types.capacity_reservation_cancellation_quote_id
    import capo_ec2.types.capacity_reservation_id


class CancelCapacityReservationRequest(TypedDict, closed=True):
    capacity_reservation_id: NotRequired[
        "capo_ec2.types.capacity_reservation_id.CapacityReservationId"
    ]
    """<p>The ID of the Capacity Reservation to be cancelled.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    apply_cancellation_charges: NotRequired[
        "capo_ec2.types.apply_cancellation_charges.ApplyCancellationCharges"
    ]
    """<p>Specifies the cancellation charge type to apply when cancelling a future-dated Capacity Reservation during its commitment duration. Possible values include <code>commitment-wind-down</code>, which continues billing for the remaining commitment duration without delivering capacity.</p>"""
    quote_id: NotRequired[
        "capo_ec2.types.capacity_reservation_cancellation_quote_id.CapacityReservationCancellationQuoteId"
    ]
    """<p>The ID of the cancellation quote to use for the cancellation. You can generate a cancellation quote by using the <code>CreateCapacityReservationCancellationQuote</code> action. The cancellation quote must be in an <code>active</code> state.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CancelCapacityReservationRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "capacity_reservation_id" in value:
        pairs.append(
            (
                f"{key_prefix}CapacityReservationId",
                str(value["capacity_reservation_id"]),
            )
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "apply_cancellation_charges" in value:
        import capo_ec2.types.apply_cancellation_charges

        capo_ec2.types.apply_cancellation_charges.serialize_ec2_query(
            value["apply_cancellation_charges"],
            pairs,
            f"{key_prefix}ApplyCancellationCharges",
        )
    if "quote_id" in value:
        pairs.append((f"{key_prefix}QuoteId", str(value["quote_id"])))


def deserialize_ec2_query(el: Element) -> CancelCapacityReservationRequest:
    out: CancelCapacityReservationRequest = {}  # type: ignore[typeddict-item]
    child_capacity_reservation_id = el.find("CapacityReservationId")
    if child_capacity_reservation_id is not None:
        out["capacity_reservation_id"] = str(child_capacity_reservation_id.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_apply_cancellation_charges = el.find("ApplyCancellationCharges")
    if child_apply_cancellation_charges is not None:
        import capo_ec2.types.apply_cancellation_charges

        out["apply_cancellation_charges"] = (
            capo_ec2.types.apply_cancellation_charges.deserialize_ec2_query(
                child_apply_cancellation_charges
            )
        )
    child_quote_id = el.find("QuoteId")
    if child_quote_id is not None:
        out["quote_id"] = str(child_quote_id.text or "")
    return out
