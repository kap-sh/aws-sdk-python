"""Generated from Smithy shape ``com.amazonaws.ec2#PurchaseHostReservationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.currency_code_values
    import aws_sdk_ec2.types.purchase_set
    import aws_sdk_ec2.types.string


class PurchaseHostReservationResult(TypedDict):
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring Idempotency</a>.</p>"""
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
