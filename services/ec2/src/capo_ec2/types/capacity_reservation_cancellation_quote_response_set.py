"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationCancellationQuoteResponseSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_reservation_cancellation_quote

CapacityReservationCancellationQuoteResponseSet: TypeAlias = list[
    "capo_ec2.types.capacity_reservation_cancellation_quote.CapacityReservationCancellationQuote"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityReservationCancellationQuoteResponseSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.capacity_reservation_cancellation_quote

        capo_ec2.types.capacity_reservation_cancellation_quote.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    el: Element,
) -> CapacityReservationCancellationQuoteResponseSet:
    import capo_ec2.types.capacity_reservation_cancellation_quote

    out: CapacityReservationCancellationQuoteResponseSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.capacity_reservation_cancellation_quote.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> CapacityReservationCancellationQuoteResponseSet:
    import capo_ec2.types.capacity_reservation_cancellation_quote

    out: CapacityReservationCancellationQuoteResponseSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.capacity_reservation_cancellation_quote.deserialize_ec2_query(
                child
            )
        )
    return out
