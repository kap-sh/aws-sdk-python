"""Generated from Smithy shape ``com.amazonaws.ec2#PurchaseHostReservationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.currency_code_values
    import aws_sdk_ec2.types.offering_id
    import aws_sdk_ec2.types.request_host_id_set
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class PurchaseHostReservationRequest(TypedDict):
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring Idempotency</a>.</p>"""
    currency_code: NotRequired[
        "aws_sdk_ec2.types.currency_code_values.CurrencyCodeValues"
    ]
    """<p>The currency in which the <code>totalUpfrontPrice</code>, <code>LimitPrice</code>, and <code>totalHourlyPrice</code> amounts are specified. At this time, the only supported currency is <code>USD</code>.</p>"""
    host_id_set: NotRequired["aws_sdk_ec2.types.request_host_id_set.RequestHostIdSet"]
    """<p>The IDs of the Dedicated Hosts with which the reservation will be associated.</p>"""
    limit_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The specified limit is checked against the total upfront cost of the reservation (calculated as the offering's upfront cost multiplied by the host count). If the total upfront cost is greater than the specified price limit, the request fails. This is used to ensure that the purchase does not exceed the expected upfront cost of the purchase. At this time, the only supported currency is <code>USD</code>. For example, to indicate a limit price of USD 100, specify 100.00.</p>"""
    offering_id: NotRequired["aws_sdk_ec2.types.offering_id.OfferingId"]
    """<p>The ID of the offering.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the Dedicated Host Reservation during purchase.</p>"""
