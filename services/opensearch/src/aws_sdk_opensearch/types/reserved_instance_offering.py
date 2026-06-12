"""Generated from Smithy shape ``com.amazonaws.opensearch#ReservedInstanceOffering``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.double
    import aws_sdk_opensearch.types.guid
    import aws_sdk_opensearch.types.integer
    import aws_sdk_opensearch.types.open_search_partition_instance_type
    import aws_sdk_opensearch.types.recurring_charge_list
    import aws_sdk_opensearch.types.reserved_instance_payment_option
    import aws_sdk_opensearch.types.string


class ReservedInstanceOffering(TypedDict):
    reserved_instance_offering_id: NotRequired["aws_sdk_opensearch.types.guid.GUID"]
    """<p>The unique identifier of the Reserved Instance offering.</p>"""
    instance_type: NotRequired[
        "aws_sdk_opensearch.types.open_search_partition_instance_type.OpenSearchPartitionInstanceType"
    ]
    """<p>The OpenSearch instance type offered by the Reserved Instance offering.</p>"""
    duration: "aws_sdk_opensearch.types.integer.Integer"
    """<p>The duration, in seconds, for which the offering will reserve the OpenSearch instance.</p>"""
    fixed_price: NotRequired["aws_sdk_opensearch.types.double.Double"]
    """<p>The upfront fixed charge you will pay to purchase the specific Reserved Instance offering.</p>"""
    usage_price: NotRequired["aws_sdk_opensearch.types.double.Double"]
    """<p>The hourly rate at which you're charged for the domain using this Reserved Instance.</p>"""
    currency_code: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p>The currency code for the Reserved Instance offering.</p>"""
    payment_option: NotRequired[
        "aws_sdk_opensearch.types.reserved_instance_payment_option.ReservedInstancePaymentOption"
    ]
    """<p>Payment option for the Reserved Instance offering</p>"""
    recurring_charges: NotRequired[
        "aws_sdk_opensearch.types.recurring_charge_list.RecurringChargeList"
    ]
    """<p>The recurring charge to your account, regardless of whether you creates any domains using the offering.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReservedInstanceOffering) -> dict:
    out: dict = {}
    if "reserved_instance_offering_id" in value:
        out["ReservedInstanceOfferingId"] = value["reserved_instance_offering_id"]
    if "instance_type" in value:
        import aws_sdk_opensearch.types.open_search_partition_instance_type

        out["InstanceType"] = (
            aws_sdk_opensearch.types.open_search_partition_instance_type.serialize_json(
                value["instance_type"]
            )
        )
    out["Duration"] = value.get("duration", 0)
    if "fixed_price" in value:
        out["FixedPrice"] = value["fixed_price"]
    if "usage_price" in value:
        out["UsagePrice"] = value["usage_price"]
    if "currency_code" in value:
        out["CurrencyCode"] = value["currency_code"]
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


def deserialize_json(data: dict) -> ReservedInstanceOffering:
    out: ReservedInstanceOffering = {}  # type: ignore[typeddict-item]
    if "ReservedInstanceOfferingId" in data:
        out["reserved_instance_offering_id"] = data["ReservedInstanceOfferingId"]
    if "InstanceType" in data:
        import aws_sdk_opensearch.types.open_search_partition_instance_type

        out["instance_type"] = (
            aws_sdk_opensearch.types.open_search_partition_instance_type.deserialize_json(
                data["InstanceType"]
            )
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
