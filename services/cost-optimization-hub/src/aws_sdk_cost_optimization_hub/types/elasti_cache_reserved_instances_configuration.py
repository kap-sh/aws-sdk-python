"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ElastiCacheReservedInstancesConfiguration``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ElastiCacheReservedInstancesConfiguration(TypedDict):
    account_scope: NotRequired["str"]
    """<p>The account scope for which you want recommendations.</p>"""
    service: NotRequired["str"]
    """<p>The service for which you want recommendations.</p>"""
    term: NotRequired["str"]
    """<p>The reserved instances recommendation term in years.</p>"""
    payment_option: NotRequired["str"]
    """<p>The payment option for the commitment.</p>"""
    reserved_instances_region: NotRequired["str"]
    """<p>The Amazon Web Services Region of the commitment.</p>"""
    upfront_cost: NotRequired["str"]
    """<p>How much purchasing this instance costs you upfront.</p>"""
    monthly_recurring_cost: NotRequired["str"]
    """<p>How much purchasing these reserved instances costs you on a monthly basis.</p>"""
    normalized_units_to_purchase: NotRequired["str"]
    """<p>The number of normalized units that Amazon Web Services recommends that you purchase.</p>"""
    number_of_instances_to_purchase: NotRequired["str"]
    """<p>The number of instances that Amazon Web Services recommends that you purchase.</p>"""
    instance_family: NotRequired["str"]
    """<p>The instance family of the recommended reservation.</p>"""
    instance_type: NotRequired["str"]
    """<p>The type of instance that Amazon Web Services recommends.</p>"""
    current_generation: NotRequired["str"]
    """<p>Determines whether the recommendation is for a current generation instance.</p>"""
    size_flex_eligible: NotRequired["bool"]
    """<p>Determines whether the recommendation is size flexible.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ElastiCacheReservedInstancesConfiguration) -> dict:
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
    if "normalized_units_to_purchase" in value:
        out["normalizedUnitsToPurchase"] = value["normalized_units_to_purchase"]
    if "number_of_instances_to_purchase" in value:
        out["numberOfInstancesToPurchase"] = value["number_of_instances_to_purchase"]
    if "instance_family" in value:
        out["instanceFamily"] = value["instance_family"]
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    if "current_generation" in value:
        out["currentGeneration"] = value["current_generation"]
    if "size_flex_eligible" in value:
        out["sizeFlexEligible"] = value["size_flex_eligible"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ElastiCacheReservedInstancesConfiguration:
    out: ElastiCacheReservedInstancesConfiguration = {}  # type: ignore[typeddict-item]
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
    if "normalizedUnitsToPurchase" in data:
        out["normalized_units_to_purchase"] = data["normalizedUnitsToPurchase"]
    if "numberOfInstancesToPurchase" in data:
        out["number_of_instances_to_purchase"] = data["numberOfInstancesToPurchase"]
    if "instanceFamily" in data:
        out["instance_family"] = data["instanceFamily"]
    if "instanceType" in data:
        out["instance_type"] = data["instanceType"]
    if "currentGeneration" in data:
        out["current_generation"] = data["currentGeneration"]
    if "sizeFlexEligible" in data:
        out["size_flex_eligible"] = data["sizeFlexEligible"]
    return out
