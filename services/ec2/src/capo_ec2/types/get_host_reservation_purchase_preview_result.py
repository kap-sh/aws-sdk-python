"""Generated from Smithy shape ``com.amazonaws.ec2#GetHostReservationPurchasePreviewResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.currency_code_values
    import capo_ec2.types.purchase_set
    import capo_ec2.types.string


class GetHostReservationPurchasePreviewResult(TypedDict, closed=True):
    currency_code: NotRequired["capo_ec2.types.currency_code_values.CurrencyCodeValues"]
    """<p>The currency in which the <code>totalUpfrontPrice</code> and <code>totalHourlyPrice</code> amounts are specified. At this time, the only supported currency is <code>USD</code>.</p>"""
    purchase: NotRequired["capo_ec2.types.purchase_set.PurchaseSet"]
    """<p>The purchase information of the Dedicated Host reservation and the Dedicated Hosts associated with it.</p>"""
    total_hourly_price: NotRequired["capo_ec2.types.string.String"]
    """<p>The potential total hourly price of the reservation per hour.</p>"""
    total_upfront_price: NotRequired["capo_ec2.types.string.String"]
    """<p>The potential total upfront price. This is billed immediately.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetHostReservationPurchasePreviewResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "currency_code" in value:
        import capo_ec2.types.currency_code_values

        capo_ec2.types.currency_code_values.serialize_ec2_query(
            value["currency_code"], pairs, f"{key_prefix}CurrencyCode"
        )
    if "purchase" in value:
        import capo_ec2.types.purchase_set

        capo_ec2.types.purchase_set.serialize_ec2_query(
            value["purchase"], pairs, f"{key_prefix}Purchase"
        )
    if "total_hourly_price" in value:
        pairs.append(
            (f"{key_prefix}TotalHourlyPrice", str(value["total_hourly_price"]))
        )
    if "total_upfront_price" in value:
        pairs.append(
            (f"{key_prefix}TotalUpfrontPrice", str(value["total_upfront_price"]))
        )


def deserialize_ec2_query(el: Element) -> GetHostReservationPurchasePreviewResult:
    out: GetHostReservationPurchasePreviewResult = {}  # type: ignore[typeddict-item]
    child_currency_code = el.find("currencyCode")
    if child_currency_code is not None:
        import capo_ec2.types.currency_code_values

        out["currency_code"] = (
            capo_ec2.types.currency_code_values.deserialize_ec2_query(
                child_currency_code
            )
        )
    if el.find("purchase") is not None:
        import capo_ec2.types.purchase_set

        out["purchase"] = capo_ec2.types.purchase_set.deserialize_ec2_query(
            el, "purchase"
        )
    child_total_hourly_price = el.find("totalHourlyPrice")
    if child_total_hourly_price is not None:
        out["total_hourly_price"] = str(child_total_hourly_price.text or "")
    child_total_upfront_price = el.find("totalUpfrontPrice")
    if child_total_upfront_price is not None:
        out["total_upfront_price"] = str(child_total_upfront_price.text or "")
    return out
