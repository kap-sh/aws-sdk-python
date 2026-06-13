"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#RdsReservedInstancesConfiguration``."""

from typing import TypedDict

from typing_extensions import NotRequired


class RdsReservedInstancesConfiguration(TypedDict):
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
    """<p>How much purchasing this instance costs you on a monthly basis.</p>"""
    normalized_units_to_purchase: NotRequired["str"]
    """<p>The number of normalized units that Amazon Web Services recommends that you purchase.</p>"""
    number_of_instances_to_purchase: NotRequired["str"]
    """<p>The number of instances that Amazon Web Services recommends that you purchase.</p>"""
    instance_family: NotRequired["str"]
    """<p>The instance family of the recommended reservation.</p>"""
    instance_type: NotRequired["str"]
    """<p>The type of instance that Amazon Web Services recommends.</p>"""
    size_flex_eligible: NotRequired["bool"]
    """<p>Determines whether the recommendation is size flexible.</p>"""
    current_generation: NotRequired["str"]
    """<p>Determines whether the recommendation is for a current generation instance.</p>"""
    license_model: NotRequired["str"]
    """<p>The license model that the recommended reservation supports.</p>"""
    database_edition: NotRequired["str"]
    """<p>The database edition that the recommended reservation supports.</p>"""
    database_engine: NotRequired["str"]
    """<p>The database engine that the recommended reservation supports.</p>"""
    deployment_option: NotRequired["str"]
    """<p>Determines whether the recommendation is for a reservation in a single Availability Zone or a reservation with a backup in a second Availability Zone.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RdsReservedInstancesConfiguration) -> dict:
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
    if "size_flex_eligible" in value:
        out["sizeFlexEligible"] = value["size_flex_eligible"]
    if "current_generation" in value:
        out["currentGeneration"] = value["current_generation"]
    if "license_model" in value:
        out["licenseModel"] = value["license_model"]
    if "database_edition" in value:
        out["databaseEdition"] = value["database_edition"]
    if "database_engine" in value:
        out["databaseEngine"] = value["database_engine"]
    if "deployment_option" in value:
        out["deploymentOption"] = value["deployment_option"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RdsReservedInstancesConfiguration:
    out: RdsReservedInstancesConfiguration = {}  # type: ignore[typeddict-item]
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
    if "sizeFlexEligible" in data:
        out["size_flex_eligible"] = data["sizeFlexEligible"]
    if "currentGeneration" in data:
        out["current_generation"] = data["currentGeneration"]
    if "licenseModel" in data:
        out["license_model"] = data["licenseModel"]
    if "databaseEdition" in data:
        out["database_edition"] = data["databaseEdition"]
    if "databaseEngine" in data:
        out["database_engine"] = data["databaseEngine"]
    if "deploymentOption" in data:
        out["deployment_option"] = data["deploymentOption"]
    return out
