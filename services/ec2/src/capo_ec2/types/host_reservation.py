"""Generated from Smithy shape ``com.amazonaws.ec2#HostReservation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.currency_code_values
    import capo_ec2.types.date_time
    import capo_ec2.types.host_reservation_id
    import capo_ec2.types.integer
    import capo_ec2.types.offering_id
    import capo_ec2.types.payment_option
    import capo_ec2.types.reservation_state
    import capo_ec2.types.response_host_id_set
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class HostReservation(TypedDict, closed=True):
    count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of Dedicated Hosts the reservation is associated with.</p>"""
    currency_code: NotRequired["capo_ec2.types.currency_code_values.CurrencyCodeValues"]
    """<p>The currency in which the <code>upfrontPrice</code> and <code>hourlyPrice</code> amounts are specified. At this time, the only supported currency is <code>USD</code>.</p>"""
    duration: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The length of the reservation's term, specified in seconds. Can be <code>31536000 (1 year)</code> | <code>94608000 (3 years)</code>.</p>"""
    end: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The date and time that the reservation ends.</p>"""
    host_id_set: NotRequired["capo_ec2.types.response_host_id_set.ResponseHostIdSet"]
    """<p>The IDs of the Dedicated Hosts associated with the reservation.</p>"""
    host_reservation_id: NotRequired[
        "capo_ec2.types.host_reservation_id.HostReservationId"
    ]
    """<p>The ID of the reservation that specifies the associated Dedicated Hosts.</p>"""
    hourly_price: NotRequired["capo_ec2.types.string.String"]
    """<p>The hourly price of the reservation.</p>"""
    instance_family: NotRequired["capo_ec2.types.string.String"]
    """<p>The instance family of the Dedicated Host Reservation. The instance family on the Dedicated Host must be the same in order for it to benefit from the reservation.</p>"""
    offering_id: NotRequired["capo_ec2.types.offering_id.OfferingId"]
    """<p>The ID of the reservation. This remains the same regardless of which Dedicated Hosts are associated with it.</p>"""
    payment_option: NotRequired["capo_ec2.types.payment_option.PaymentOption"]
    """<p>The payment option selected for this reservation.</p>"""
    start: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The date and time that the reservation started.</p>"""
    state: NotRequired["capo_ec2.types.reservation_state.ReservationState"]
    """<p>The state of the reservation.</p>"""
    upfront_price: NotRequired["capo_ec2.types.string.String"]
    """<p>The upfront price of the reservation.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the Dedicated Host Reservation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: HostReservation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "count" in value:
        pairs.append((f"{key_prefix}Count", str(value["count"])))
    if "currency_code" in value:
        import capo_ec2.types.currency_code_values

        capo_ec2.types.currency_code_values.serialize_ec2_query(
            value["currency_code"], pairs, f"{key_prefix}CurrencyCode"
        )
    if "duration" in value:
        pairs.append((f"{key_prefix}Duration", str(value["duration"])))
    if "end" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["end"], pairs, f"{key_prefix}End"
        )
    if "host_id_set" in value:
        import capo_ec2.types.response_host_id_set

        capo_ec2.types.response_host_id_set.serialize_ec2_query(
            value["host_id_set"], pairs, f"{key_prefix}HostIdSet"
        )
    if "host_reservation_id" in value:
        pairs.append(
            (f"{key_prefix}HostReservationId", str(value["host_reservation_id"]))
        )
    if "hourly_price" in value:
        pairs.append((f"{key_prefix}HourlyPrice", str(value["hourly_price"])))
    if "instance_family" in value:
        pairs.append((f"{key_prefix}InstanceFamily", str(value["instance_family"])))
    if "offering_id" in value:
        pairs.append((f"{key_prefix}OfferingId", str(value["offering_id"])))
    if "payment_option" in value:
        import capo_ec2.types.payment_option

        capo_ec2.types.payment_option.serialize_ec2_query(
            value["payment_option"], pairs, f"{key_prefix}PaymentOption"
        )
    if "start" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["start"], pairs, f"{key_prefix}Start"
        )
    if "state" in value:
        import capo_ec2.types.reservation_state

        capo_ec2.types.reservation_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "upfront_price" in value:
        pairs.append((f"{key_prefix}UpfrontPrice", str(value["upfront_price"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> HostReservation:
    out: HostReservation = {}  # type: ignore[typeddict-item]
    child_count = el.find("Count")
    if child_count is not None:
        out["count"] = int(child_count.text or "")
    child_currency_code = el.find("CurrencyCode")
    if child_currency_code is not None:
        import capo_ec2.types.currency_code_values

        out["currency_code"] = (
            capo_ec2.types.currency_code_values.deserialize_ec2_query(
                child_currency_code
            )
        )
    child_duration = el.find("Duration")
    if child_duration is not None:
        out["duration"] = int(child_duration.text or "")
    child_end = el.find("End")
    if child_end is not None:
        import capo_ec2.types.date_time

        out["end"] = capo_ec2.types.date_time.deserialize_ec2_query(child_end)
    if el.find("HostIdSet") is not None:
        import capo_ec2.types.response_host_id_set

        out["host_id_set"] = capo_ec2.types.response_host_id_set.deserialize_ec2_query(
            el, "HostIdSet"
        )
    child_host_reservation_id = el.find("HostReservationId")
    if child_host_reservation_id is not None:
        out["host_reservation_id"] = str(child_host_reservation_id.text or "")
    child_hourly_price = el.find("HourlyPrice")
    if child_hourly_price is not None:
        out["hourly_price"] = str(child_hourly_price.text or "")
    child_instance_family = el.find("InstanceFamily")
    if child_instance_family is not None:
        out["instance_family"] = str(child_instance_family.text or "")
    child_offering_id = el.find("OfferingId")
    if child_offering_id is not None:
        out["offering_id"] = str(child_offering_id.text or "")
    child_payment_option = el.find("PaymentOption")
    if child_payment_option is not None:
        import capo_ec2.types.payment_option

        out["payment_option"] = capo_ec2.types.payment_option.deserialize_ec2_query(
            child_payment_option
        )
    child_start = el.find("Start")
    if child_start is not None:
        import capo_ec2.types.date_time

        out["start"] = capo_ec2.types.date_time.deserialize_ec2_query(child_start)
    child_state = el.find("State")
    if child_state is not None:
        import capo_ec2.types.reservation_state

        out["state"] = capo_ec2.types.reservation_state.deserialize_ec2_query(
            child_state
        )
    child_upfront_price = el.find("UpfrontPrice")
    if child_upfront_price is not None:
        out["upfront_price"] = str(child_upfront_price.text or "")
    if el.find("TagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
