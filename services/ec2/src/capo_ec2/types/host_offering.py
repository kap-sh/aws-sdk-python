"""Generated from Smithy shape ``com.amazonaws.ec2#HostOffering``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.currency_code_values
    import capo_ec2.types.integer
    import capo_ec2.types.offering_id
    import capo_ec2.types.payment_option
    import capo_ec2.types.string


class HostOffering(TypedDict, closed=True):
    currency_code: NotRequired["capo_ec2.types.currency_code_values.CurrencyCodeValues"]
    """<p>The currency of the offering.</p>"""
    duration: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The duration of the offering (in seconds).</p>"""
    hourly_price: NotRequired["capo_ec2.types.string.String"]
    """<p>The hourly price of the offering.</p>"""
    instance_family: NotRequired["capo_ec2.types.string.String"]
    """<p>The instance family of the offering.</p>"""
    offering_id: NotRequired["capo_ec2.types.offering_id.OfferingId"]
    """<p>The ID of the offering.</p>"""
    payment_option: NotRequired["capo_ec2.types.payment_option.PaymentOption"]
    """<p>The available payment option.</p>"""
    upfront_price: NotRequired["capo_ec2.types.string.String"]
    """<p>The upfront price of the offering. Does not apply to No Upfront offerings.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: HostOffering, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "currency_code" in value:
        import capo_ec2.types.currency_code_values

        capo_ec2.types.currency_code_values.serialize_ec2_query(
            value["currency_code"], pairs, f"{key_prefix}CurrencyCode"
        )
    if "duration" in value:
        pairs.append((f"{key_prefix}Duration", str(value["duration"])))
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
    if "upfront_price" in value:
        pairs.append((f"{key_prefix}UpfrontPrice", str(value["upfront_price"])))


def deserialize_ec2_query(el: Element) -> HostOffering:
    out: HostOffering = {}  # type: ignore[typeddict-item]
    child_currency_code = el.find("currencyCode")
    if child_currency_code is not None:
        import capo_ec2.types.currency_code_values

        out["currency_code"] = (
            capo_ec2.types.currency_code_values.deserialize_ec2_query(
                child_currency_code
            )
        )
    child_duration = el.find("duration")
    if child_duration is not None:
        out["duration"] = int(child_duration.text or "")
    child_hourly_price = el.find("hourlyPrice")
    if child_hourly_price is not None:
        out["hourly_price"] = str(child_hourly_price.text or "")
    child_instance_family = el.find("instanceFamily")
    if child_instance_family is not None:
        out["instance_family"] = str(child_instance_family.text or "")
    child_offering_id = el.find("offeringId")
    if child_offering_id is not None:
        out["offering_id"] = str(child_offering_id.text or "")
    child_payment_option = el.find("paymentOption")
    if child_payment_option is not None:
        import capo_ec2.types.payment_option

        out["payment_option"] = capo_ec2.types.payment_option.deserialize_ec2_query(
            child_payment_option
        )
    child_upfront_price = el.find("upfrontPrice")
    if child_upfront_price is not None:
        out["upfront_price"] = str(child_upfront_price.text or "")
    return out
