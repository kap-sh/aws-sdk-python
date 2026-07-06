"""Generated from Smithy shape ``com.amazonaws.ec2#Purchase``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.currency_code_values
    import aws_sdk_ec2.types.host_reservation_id
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.payment_option
    import aws_sdk_ec2.types.response_host_id_set
    import aws_sdk_ec2.types.string


class Purchase(TypedDict, closed=True):
    currency_code: NotRequired[
        "aws_sdk_ec2.types.currency_code_values.CurrencyCodeValues"
    ]
    """<p>The currency in which the <code>UpfrontPrice</code> and <code>HourlyPrice</code> amounts are specified. At this time, the only supported currency is <code>USD</code>.</p>"""
    duration: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The duration of the reservation's term in seconds.</p>"""
    host_id_set: NotRequired["aws_sdk_ec2.types.response_host_id_set.ResponseHostIdSet"]
    """<p>The IDs of the Dedicated Hosts associated with the reservation.</p>"""
    host_reservation_id: NotRequired[
        "aws_sdk_ec2.types.host_reservation_id.HostReservationId"
    ]
    """<p>The ID of the reservation.</p>"""
    hourly_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The hourly price of the reservation per hour.</p>"""
    instance_family: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The instance family on the Dedicated Host that the reservation can be associated with.</p>"""
    payment_option: NotRequired["aws_sdk_ec2.types.payment_option.PaymentOption"]
    """<p>The payment option for the reservation.</p>"""
    upfront_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The upfront price of the reservation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Purchase, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "currency_code" in value:
        import aws_sdk_ec2.types.currency_code_values

        aws_sdk_ec2.types.currency_code_values.serialize_ec2_query(
            value["currency_code"], pairs, f"{prefix}.CurrencyCode"
        )
    if "duration" in value:
        pairs.append((f"{prefix}.Duration", str(value["duration"])))
    if "host_id_set" in value:
        import aws_sdk_ec2.types.response_host_id_set

        aws_sdk_ec2.types.response_host_id_set.serialize_ec2_query(
            value["host_id_set"], pairs, f"{prefix}.HostIdSet"
        )
    if "host_reservation_id" in value:
        pairs.append((f"{prefix}.HostReservationId", str(value["host_reservation_id"])))
    if "hourly_price" in value:
        pairs.append((f"{prefix}.HourlyPrice", str(value["hourly_price"])))
    if "instance_family" in value:
        pairs.append((f"{prefix}.InstanceFamily", str(value["instance_family"])))
    if "payment_option" in value:
        import aws_sdk_ec2.types.payment_option

        aws_sdk_ec2.types.payment_option.serialize_ec2_query(
            value["payment_option"], pairs, f"{prefix}.PaymentOption"
        )
    if "upfront_price" in value:
        pairs.append((f"{prefix}.UpfrontPrice", str(value["upfront_price"])))


def deserialize_ec2_query(el: Element) -> Purchase:
    out: Purchase = {}  # type: ignore[typeddict-item]
    child_currency_code = el.find("CurrencyCode")
    if child_currency_code is not None:
        import aws_sdk_ec2.types.currency_code_values

        out["currency_code"] = (
            aws_sdk_ec2.types.currency_code_values.deserialize_ec2_query(
                child_currency_code
            )
        )
    child_duration = el.find("Duration")
    if child_duration is not None:
        out["duration"] = int(child_duration.text or "")
    if el.find("HostIdSet") is not None:
        import aws_sdk_ec2.types.response_host_id_set

        out["host_id_set"] = (
            aws_sdk_ec2.types.response_host_id_set.deserialize_ec2_query(
                el, "HostIdSet"
            )
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
    child_payment_option = el.find("PaymentOption")
    if child_payment_option is not None:
        import aws_sdk_ec2.types.payment_option

        out["payment_option"] = aws_sdk_ec2.types.payment_option.deserialize_ec2_query(
            child_payment_option
        )
    child_upfront_price = el.find("UpfrontPrice")
    if child_upfront_price is not None:
        out["upfront_price"] = str(child_upfront_price.text or "")
    return out
