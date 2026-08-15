"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationCancellationQuote``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.cancellation_terms_set
    import capo_ec2.types.capacity_reservation_cancellation_quote_id
    import capo_ec2.types.capacity_reservation_cancellation_quote_state
    import capo_ec2.types.capacity_reservation_configuration
    import capo_ec2.types.capacity_reservation_id
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.tag_list


class CapacityReservationCancellationQuote(TypedDict, closed=True):
    capacity_reservation_cancellation_quote_id: NotRequired[
        "capo_ec2.types.capacity_reservation_cancellation_quote_id.CapacityReservationCancellationQuoteId"
    ]
    """<p>The ID of the cancellation quote.</p>"""
    capacity_reservation_id: NotRequired[
        "capo_ec2.types.capacity_reservation_id.CapacityReservationId"
    ]
    """<p>The ID of the Capacity Reservation associated with the cancellation quote.</p>"""
    create_time: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The date and time at which the cancellation quote was created.</p>"""
    expiration_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time at which the cancellation quote expires.</p>"""
    quote_state: NotRequired[
        "capo_ec2.types.capacity_reservation_cancellation_quote_state.CapacityReservationCancellationQuoteState"
    ]
    """<p>The state of the cancellation quote. Possible values include <code>pending</code>, <code>active</code>, and <code>expired</code>.</p>"""
    current_configuration: NotRequired[
        "capo_ec2.types.capacity_reservation_configuration.CapacityReservationConfiguration"
    ]
    """<p>The current configuration of the Capacity Reservation.</p>"""
    cancellation_terms: NotRequired[
        "capo_ec2.types.cancellation_terms_set.CancellationTermsSet"
    ]
    """<p>The cancellation terms associated with the quote, including the fee type and charge details.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the cancellation quote.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityReservationCancellationQuote,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "capacity_reservation_cancellation_quote_id" in value:
        pairs.append(
            (
                f"{key_prefix}CapacityReservationCancellationQuoteId",
                str(value["capacity_reservation_cancellation_quote_id"]),
            )
        )
    if "capacity_reservation_id" in value:
        pairs.append(
            (
                f"{key_prefix}CapacityReservationId",
                str(value["capacity_reservation_id"]),
            )
        )
    if "create_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["create_time"], pairs, f"{key_prefix}CreateTime"
        )
    if "expiration_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["expiration_time"], pairs, f"{key_prefix}ExpirationTime"
        )
    if "quote_state" in value:
        import capo_ec2.types.capacity_reservation_cancellation_quote_state

        capo_ec2.types.capacity_reservation_cancellation_quote_state.serialize_ec2_query(
            value["quote_state"], pairs, f"{key_prefix}QuoteState"
        )
    if "current_configuration" in value:
        import capo_ec2.types.capacity_reservation_configuration

        capo_ec2.types.capacity_reservation_configuration.serialize_ec2_query(
            value["current_configuration"], pairs, f"{key_prefix}CurrentConfiguration"
        )
    if "cancellation_terms" in value:
        import capo_ec2.types.cancellation_terms_set

        capo_ec2.types.cancellation_terms_set.serialize_ec2_query(
            value["cancellation_terms"], pairs, f"{key_prefix}CancellationTermSet"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> CapacityReservationCancellationQuote:
    out: CapacityReservationCancellationQuote = {}  # type: ignore[typeddict-item]
    child_capacity_reservation_cancellation_quote_id = el.find(
        "capacityReservationCancellationQuoteId"
    )
    if child_capacity_reservation_cancellation_quote_id is not None:
        out["capacity_reservation_cancellation_quote_id"] = str(
            child_capacity_reservation_cancellation_quote_id.text or ""
        )
    child_capacity_reservation_id = el.find("capacityReservationId")
    if child_capacity_reservation_id is not None:
        out["capacity_reservation_id"] = str(child_capacity_reservation_id.text or "")
    child_create_time = el.find("createTime")
    if child_create_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["create_time"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_create_time
        )
    child_expiration_time = el.find("expirationTime")
    if child_expiration_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["expiration_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_expiration_time
            )
        )
    child_quote_state = el.find("quoteState")
    if child_quote_state is not None:
        import capo_ec2.types.capacity_reservation_cancellation_quote_state

        out["quote_state"] = (
            capo_ec2.types.capacity_reservation_cancellation_quote_state.deserialize_ec2_query(
                child_quote_state
            )
        )
    child_current_configuration = el.find("currentConfiguration")
    if child_current_configuration is not None:
        import capo_ec2.types.capacity_reservation_configuration

        out["current_configuration"] = (
            capo_ec2.types.capacity_reservation_configuration.deserialize_ec2_query(
                child_current_configuration
            )
        )
    child_cancellation_terms = el.find("cancellationTermSet")
    if child_cancellation_terms is not None:
        import capo_ec2.types.cancellation_terms_set

        out["cancellation_terms"] = (
            capo_ec2.types.cancellation_terms_set.deserialize_ec2_query(
                child_cancellation_terms
            )
        )
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    return out
