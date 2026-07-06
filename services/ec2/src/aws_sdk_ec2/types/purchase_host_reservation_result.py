"""Generated from Smithy shape ``com.amazonaws.ec2#PurchaseHostReservationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.currency_code_values
    import aws_sdk_ec2.types.purchase_set
    import aws_sdk_ec2.types.string


class PurchaseHostReservationResult(TypedDict, closed=True):
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    r"""<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring Idempotency</a>.</p>"""
    currency_code: NotRequired[
        "aws_sdk_ec2.types.currency_code_values.CurrencyCodeValues"
    ]
    """<p>The currency in which the <code>totalUpfrontPrice</code> and <code>totalHourlyPrice</code> amounts are specified. At this time, the only supported currency is <code>USD</code>.</p>"""
    purchase: NotRequired["aws_sdk_ec2.types.purchase_set.PurchaseSet"]
    """<p>Describes the details of the purchase.</p>"""
    total_hourly_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The total hourly price of the reservation calculated per hour.</p>"""
    total_upfront_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The total amount charged to your account when you purchase the reservation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PurchaseHostReservationResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))
    if "currency_code" in value:
        import aws_sdk_ec2.types.currency_code_values

        aws_sdk_ec2.types.currency_code_values.serialize_ec2_query(
            value["currency_code"], pairs, f"{prefix}.CurrencyCode"
        )
    if "purchase" in value:
        import aws_sdk_ec2.types.purchase_set

        aws_sdk_ec2.types.purchase_set.serialize_ec2_query(
            value["purchase"], pairs, f"{prefix}.Purchase"
        )
    if "total_hourly_price" in value:
        pairs.append((f"{prefix}.TotalHourlyPrice", str(value["total_hourly_price"])))
    if "total_upfront_price" in value:
        pairs.append((f"{prefix}.TotalUpfrontPrice", str(value["total_upfront_price"])))


def deserialize_ec2_query(el: Element) -> PurchaseHostReservationResult:
    out: PurchaseHostReservationResult = {}  # type: ignore[typeddict-item]
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_currency_code = el.find("CurrencyCode")
    if child_currency_code is not None:
        import aws_sdk_ec2.types.currency_code_values

        out["currency_code"] = (
            aws_sdk_ec2.types.currency_code_values.deserialize_ec2_query(
                child_currency_code
            )
        )
    if el.find("Purchase") is not None:
        import aws_sdk_ec2.types.purchase_set

        out["purchase"] = aws_sdk_ec2.types.purchase_set.deserialize_ec2_query(
            el, "Purchase"
        )
    child_total_hourly_price = el.find("TotalHourlyPrice")
    if child_total_hourly_price is not None:
        out["total_hourly_price"] = str(child_total_hourly_price.text or "")
    child_total_upfront_price = el.find("TotalUpfrontPrice")
    if child_total_upfront_price is not None:
        out["total_upfront_price"] = str(child_total_upfront_price.text or "")
    return out
