"""Generated from Smithy shape ``com.amazonaws.outposts#Subscription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.currency_code
    import aws_sdk_outposts.types.iso8601_timestamp
    import aws_sdk_outposts.types.nullable_double
    import aws_sdk_outposts.types.order_id_list
    import aws_sdk_outposts.types.string
    import aws_sdk_outposts.types.subscription_status
    import aws_sdk_outposts.types.subscription_type


class Subscription(TypedDict, closed=True):
    subscription_id: NotRequired["aws_sdk_outposts.types.string.String"]
    """<p>The ID of the subscription that appears on the Amazon Web Services Billing Center console.</p>"""
    subscription_type: NotRequired[
        "aws_sdk_outposts.types.subscription_type.SubscriptionType"
    ]
    """<p>The type of subscription which can be one of the following:</p> <ul> <li> <p> <b>ORIGINAL</b> - The first order on the Amazon Web Services Outposts.</p> </li> <li> <p> <b>RENEWAL</b> - Renewal requests, both month to month and longer term.</p> </li> <li> <p> <b>CAPACITY_INCREASE</b> - Capacity scaling orders.</p> </li> </ul>"""
    subscription_status: NotRequired[
        "aws_sdk_outposts.types.subscription_status.SubscriptionStatus"
    ]
    """<p>The status of subscription which can be one of the following:</p> <ul> <li> <p> <b>INACTIVE</b> - Subscription requests that are inactive.</p> </li> <li> <p> <b>ACTIVE</b> - Subscription requests that are in progress and have an end date in the future.</p> </li> <li> <p> <b>PENDING</b> - Subscription has been created but billing has not yet commenced because the subscription begin date has not been reached.</p> </li> <li> <p> <b>CANCELLED</b> - Subscription requests that are cancelled.</p> </li> </ul>"""
    order_ids: NotRequired["aws_sdk_outposts.types.order_id_list.OrderIdList"]
    """<p>The order ID for your subscription.</p>"""
    begin_date: NotRequired["aws_sdk_outposts.types.iso8601_timestamp.ISO8601Timestamp"]
    """<p>The date your subscription starts.</p>"""
    end_date: NotRequired["aws_sdk_outposts.types.iso8601_timestamp.ISO8601Timestamp"]
    """<p>The date your subscription ends.</p>"""
    currency: NotRequired["aws_sdk_outposts.types.currency_code.CurrencyCode"]
    """<p>The currency of the subscription price. Currently only <code>USD</code> is supported.</p>"""
    monthly_recurring_price: NotRequired[
        "aws_sdk_outposts.types.nullable_double.NullableDouble"
    ]
    """<p>The amount you are billed each month in the subscription period.</p>"""
    upfront_price: NotRequired["aws_sdk_outposts.types.nullable_double.NullableDouble"]
    """<p>The amount billed when the subscription is created. This is a one-time charge.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Subscription) -> dict:
    out: dict = {}
    if "subscription_id" in value:
        out["SubscriptionId"] = value["subscription_id"]
    if "subscription_type" in value:
        import aws_sdk_outposts.types.subscription_type

        out["SubscriptionType"] = (
            aws_sdk_outposts.types.subscription_type.serialize_json(
                value["subscription_type"]
            )
        )
    if "subscription_status" in value:
        import aws_sdk_outposts.types.subscription_status

        out["SubscriptionStatus"] = (
            aws_sdk_outposts.types.subscription_status.serialize_json(
                value["subscription_status"]
            )
        )
    if "order_ids" in value:
        import aws_sdk_outposts.types.order_id_list

        out["OrderIds"] = aws_sdk_outposts.types.order_id_list.serialize_json(
            value["order_ids"]
        )
    if "begin_date" in value:
        import aws_sdk_outposts.types.iso8601_timestamp

        out["BeginDate"] = aws_sdk_outposts.types.iso8601_timestamp.serialize_json(
            value["begin_date"]
        )
    if "end_date" in value:
        import aws_sdk_outposts.types.iso8601_timestamp

        out["EndDate"] = aws_sdk_outposts.types.iso8601_timestamp.serialize_json(
            value["end_date"]
        )
    if "currency" in value:
        import aws_sdk_outposts.types.currency_code

        out["Currency"] = aws_sdk_outposts.types.currency_code.serialize_json(
            value["currency"]
        )
    if "monthly_recurring_price" in value:
        out["MonthlyRecurringPrice"] = value["monthly_recurring_price"]
    if "upfront_price" in value:
        out["UpfrontPrice"] = value["upfront_price"]
    return out


def deserialize_json(data: dict) -> Subscription:
    out: Subscription = {}  # type: ignore[typeddict-item]
    if "SubscriptionId" in data:
        out["subscription_id"] = data["SubscriptionId"]
    if "SubscriptionType" in data:
        import aws_sdk_outposts.types.subscription_type

        out["subscription_type"] = (
            aws_sdk_outposts.types.subscription_type.deserialize_json(
                data["SubscriptionType"]
            )
        )
    if "SubscriptionStatus" in data:
        import aws_sdk_outposts.types.subscription_status

        out["subscription_status"] = (
            aws_sdk_outposts.types.subscription_status.deserialize_json(
                data["SubscriptionStatus"]
            )
        )
    if "OrderIds" in data:
        import aws_sdk_outposts.types.order_id_list

        out["order_ids"] = aws_sdk_outposts.types.order_id_list.deserialize_json(
            data["OrderIds"]
        )
    if "BeginDate" in data:
        import aws_sdk_outposts.types.iso8601_timestamp

        out["begin_date"] = aws_sdk_outposts.types.iso8601_timestamp.deserialize_json(
            data["BeginDate"]
        )
    if "EndDate" in data:
        import aws_sdk_outposts.types.iso8601_timestamp

        out["end_date"] = aws_sdk_outposts.types.iso8601_timestamp.deserialize_json(
            data["EndDate"]
        )
    if "Currency" in data:
        import aws_sdk_outposts.types.currency_code

        out["currency"] = aws_sdk_outposts.types.currency_code.deserialize_json(
            data["Currency"]
        )
    if "MonthlyRecurringPrice" in data:
        out["monthly_recurring_price"] = data["MonthlyRecurringPrice"]
    if "UpfrontPrice" in data:
        out["upfront_price"] = data["UpfrontPrice"]
    return out
