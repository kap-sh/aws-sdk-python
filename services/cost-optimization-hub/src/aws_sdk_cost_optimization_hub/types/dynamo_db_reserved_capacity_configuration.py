"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#DynamoDbReservedCapacityConfiguration``."""

from typing import TypedDict

from typing_extensions import NotRequired


class DynamoDbReservedCapacityConfiguration(TypedDict):
    account_scope: NotRequired["str"]
    """<p>The account scope for which you want recommendations.</p>"""
    service: NotRequired["str"]
    """<p>The service for which you want recommendations.</p>"""
    term: NotRequired["str"]
    """<p>The reserved capacity recommendation term in years.</p>"""
    payment_option: NotRequired["str"]
    """<p>The payment option for the commitment.</p>"""
    reserved_instances_region: NotRequired["str"]
    """<p>The Amazon Web Services Region of the commitment.</p>"""
    upfront_cost: NotRequired["str"]
    """<p>How much purchasing this reserved capacity costs you upfront.</p>"""
    monthly_recurring_cost: NotRequired["str"]
    """<p>How much purchasing this reserved capacity costs you on a monthly basis.</p>"""
    number_of_capacity_units_to_purchase: NotRequired["str"]
    """<p>The number of reserved capacity units that Amazon Web Services recommends that you purchase.</p>"""
    capacity_units: NotRequired["str"]
    """<p>The capacity unit of the recommended reservation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DynamoDbReservedCapacityConfiguration) -> dict:
    out: dict = {}
    if "account_scope" in value:
        out["accountScope"] = value["account_scope"]
    if "service" in value:
        out["service"] = value["service"]
    if "term" in value:
        out["term"] = value["term"]
    if "payment_option" in value:
        out["paymentOption"] = value["payment_option"]
    if "reserved_instances_region" in value:
        out["reservedInstancesRegion"] = value["reserved_instances_region"]
    if "upfront_cost" in value:
        out["upfrontCost"] = value["upfront_cost"]
    if "monthly_recurring_cost" in value:
        out["monthlyRecurringCost"] = value["monthly_recurring_cost"]
    if "number_of_capacity_units_to_purchase" in value:
        out["numberOfCapacityUnitsToPurchase"] = value[
            "number_of_capacity_units_to_purchase"
        ]
    if "capacity_units" in value:
        out["capacityUnits"] = value["capacity_units"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DynamoDbReservedCapacityConfiguration:
    out: DynamoDbReservedCapacityConfiguration = {}  # type: ignore[typeddict-item]
    if "accountScope" in data:
        out["account_scope"] = data["accountScope"]
    if "service" in data:
        out["service"] = data["service"]
    if "term" in data:
        out["term"] = data["term"]
    if "paymentOption" in data:
        out["payment_option"] = data["paymentOption"]
    if "reservedInstancesRegion" in data:
        out["reserved_instances_region"] = data["reservedInstancesRegion"]
    if "upfrontCost" in data:
        out["upfront_cost"] = data["upfrontCost"]
    if "monthlyRecurringCost" in data:
        out["monthly_recurring_cost"] = data["monthlyRecurringCost"]
    if "numberOfCapacityUnitsToPurchase" in data:
        out["number_of_capacity_units_to_purchase"] = data[
            "numberOfCapacityUnitsToPurchase"
        ]
    if "capacityUnits" in data:
        out["capacity_units"] = data["capacityUnits"]
    return out
