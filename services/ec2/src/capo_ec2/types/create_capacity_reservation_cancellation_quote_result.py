"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCapacityReservationCancellationQuoteResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_reservation_cancellation_quote


class CreateCapacityReservationCancellationQuoteResult(TypedDict, closed=True):
    capacity_reservation_cancellation_quote: NotRequired[
        "capo_ec2.types.capacity_reservation_cancellation_quote.CapacityReservationCancellationQuote"
    ]
    """<p>Information about the Capacity Reservation cancellation quote.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateCapacityReservationCancellationQuoteResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "capacity_reservation_cancellation_quote" in value:
        import capo_ec2.types.capacity_reservation_cancellation_quote

        capo_ec2.types.capacity_reservation_cancellation_quote.serialize_ec2_query(
            value["capacity_reservation_cancellation_quote"],
            pairs,
            f"{key_prefix}CapacityReservationCancellationQuote",
        )


def deserialize_ec2_query(
    el: Element,
) -> CreateCapacityReservationCancellationQuoteResult:
    out: CreateCapacityReservationCancellationQuoteResult = {}  # type: ignore[typeddict-item]
    child_capacity_reservation_cancellation_quote = el.find(
        "capacityReservationCancellationQuote"
    )
    if child_capacity_reservation_cancellation_quote is not None:
        import capo_ec2.types.capacity_reservation_cancellation_quote

        out["capacity_reservation_cancellation_quote"] = (
            capo_ec2.types.capacity_reservation_cancellation_quote.deserialize_ec2_query(
                child_capacity_reservation_cancellation_quote
            )
        )
    return out
