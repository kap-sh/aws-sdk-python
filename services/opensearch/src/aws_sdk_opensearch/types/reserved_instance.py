"""Generated from Smithy shape ``com.amazonaws.opensearch#ReservedInstance``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.double
    import aws_sdk_opensearch.types.guid
    import aws_sdk_opensearch.types.integer
    import aws_sdk_opensearch.types.long
    import aws_sdk_opensearch.types.open_search_partition_instance_type
    import aws_sdk_opensearch.types.recurring_charge_list
    import aws_sdk_opensearch.types.reservation_token
    import aws_sdk_opensearch.types.reserved_instance_payment_option
    import aws_sdk_opensearch.types.string
    import aws_sdk_opensearch.types.update_timestamp


class ReservedInstance(TypedDict):
    reservation_name: NotRequired[
        "aws_sdk_opensearch.types.reservation_token.ReservationToken"
    ]
    """<p>The customer-specified identifier to track this reservation.</p>"""
    reserved_instance_id: NotRequired["aws_sdk_opensearch.types.guid.GUID"]
    """<p>The unique identifier for the reservation.</p>"""
    billing_subscription_id: NotRequired["aws_sdk_opensearch.types.long.Long"]
    """<p>The unique identifier of the billing subscription.</p>"""
    reserved_instance_offering_id: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p>The unique identifier of the Reserved Instance offering.</p>"""
    instance_type: NotRequired[
        "aws_sdk_opensearch.types.open_search_partition_instance_type.OpenSearchPartitionInstanceType"
    ]
    """<p>The OpenSearch instance type offered by theReserved Instance offering.</p>"""
    start_time: NotRequired["aws_sdk_opensearch.types.update_timestamp.UpdateTimestamp"]
    """<p>The date and time when the reservation was purchased.</p>"""
    duration: "aws_sdk_opensearch.types.integer.Integer"
    """<p>The duration, in seconds, for which the OpenSearch instance is reserved.</p>"""
    fixed_price: NotRequired["aws_sdk_opensearch.types.double.Double"]
    """<p>The upfront fixed charge you will paid to purchase the specific Reserved Instance offering.</p>"""
    usage_price: NotRequired["aws_sdk_opensearch.types.double.Double"]
    """<p>The hourly rate at which you're charged for the domain using this Reserved Instance.</p>"""
    currency_code: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p>The currency code for the offering.</p>"""
    instance_count: "aws_sdk_opensearch.types.integer.Integer"
    """<p>The number of OpenSearch instances that have been reserved.</p>"""
    state: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p>The state of the Reserved Instance.</p>"""
    payment_option: NotRequired[
        "aws_sdk_opensearch.types.reserved_instance_payment_option.ReservedInstancePaymentOption"
    ]
    """<p>The payment option as defined in the Reserved Instance offering.</p>"""
    recurring_charges: NotRequired[
        "aws_sdk_opensearch.types.recurring_charge_list.RecurringChargeList"
    ]
    """<p>The recurring charge to your account, regardless of whether you create any domains using the Reserved Instance offering.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReservedInstance) -> dict:
    out: dict = {}
    if "reservation_name" in value:
        out["ReservationName"] = value["reservation_name"]
    if "reserved_instance_id" in value:
        out["ReservedInstanceId"] = value["reserved_instance_id"]
    if "billing_subscription_id" in value:
        out["BillingSubscriptionId"] = value["billing_subscription_id"]
    if "reserved_instance_offering_id" in value:
        out["ReservedInstanceOfferingId"] = value["reserved_instance_offering_id"]
    if "instance_type" in value:
        import aws_sdk_opensearch.types.open_search_partition_instance_type

        out["InstanceType"] = (
            aws_sdk_opensearch.types.open_search_partition_instance_type.serialize_json(
                value["instance_type"]
            )
        )
    if "start_time" in value:
        import aws_sdk_opensearch.types.update_timestamp

        out["StartTime"] = aws_sdk_opensearch.types.update_timestamp.serialize_json(
            value["start_time"]
        )
    out["Duration"] = value.get("duration", 0)
    if "fixed_price" in value:
        out["FixedPrice"] = value["fixed_price"]
    if "usage_price" in value:
        out["UsagePrice"] = value["usage_price"]
    if "currency_code" in value:
        out["CurrencyCode"] = value["currency_code"]
    out["InstanceCount"] = value.get("instance_count", 0)
    if "state" in value:
        out["State"] = value["state"]
    if "payment_option" in value:
        import aws_sdk_opensearch.types.reserved_instance_payment_option

        out["PaymentOption"] = (
            aws_sdk_opensearch.types.reserved_instance_payment_option.serialize_json(
                value["payment_option"]
            )
        )
    if "recurring_charges" in value:
        import aws_sdk_opensearch.types.recurring_charge_list

        out["RecurringCharges"] = (
            aws_sdk_opensearch.types.recurring_charge_list.serialize_json(
                value["recurring_charges"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReservedInstance:
    out: ReservedInstance = {}  # type: ignore[typeddict-item]
    if "ReservationName" in data:
        out["reservation_name"] = data["ReservationName"]
    if "ReservedInstanceId" in data:
        out["reserved_instance_id"] = data["ReservedInstanceId"]
    if "BillingSubscriptionId" in data:
        out["billing_subscription_id"] = data["BillingSubscriptionId"]
    if "ReservedInstanceOfferingId" in data:
        out["reserved_instance_offering_id"] = data["ReservedInstanceOfferingId"]
    if "InstanceType" in data:
        import aws_sdk_opensearch.types.open_search_partition_instance_type

        out["instance_type"] = (
            aws_sdk_opensearch.types.open_search_partition_instance_type.deserialize_json(
                data["InstanceType"]
            )
        )
    if "StartTime" in data:
        import aws_sdk_opensearch.types.update_timestamp

        out["start_time"] = aws_sdk_opensearch.types.update_timestamp.deserialize_json(
            data["StartTime"]
        )
    if "Duration" in data:
        out["duration"] = data["Duration"]
    else:
        out["duration"] = 0
    if "FixedPrice" in data:
        out["fixed_price"] = data["FixedPrice"]
    if "UsagePrice" in data:
        out["usage_price"] = data["UsagePrice"]
    if "CurrencyCode" in data:
        out["currency_code"] = data["CurrencyCode"]
    if "InstanceCount" in data:
        out["instance_count"] = data["InstanceCount"]
    else:
        out["instance_count"] = 0
    if "State" in data:
        out["state"] = data["State"]
    if "PaymentOption" in data:
        import aws_sdk_opensearch.types.reserved_instance_payment_option

        out["payment_option"] = (
            aws_sdk_opensearch.types.reserved_instance_payment_option.deserialize_json(
                data["PaymentOption"]
            )
        )
    if "RecurringCharges" in data:
        import aws_sdk_opensearch.types.recurring_charge_list

        out["recurring_charges"] = (
            aws_sdk_opensearch.types.recurring_charge_list.deserialize_json(
                data["RecurringCharges"]
            )
        )
    return out
