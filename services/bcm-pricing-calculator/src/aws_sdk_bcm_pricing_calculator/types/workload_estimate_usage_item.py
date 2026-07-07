"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#WorkloadEstimateUsageItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.account_id
    import aws_sdk_bcm_pricing_calculator.types.currency_code
    import aws_sdk_bcm_pricing_calculator.types.historical_usage_entity
    import aws_sdk_bcm_pricing_calculator.types.operation
    import aws_sdk_bcm_pricing_calculator.types.resource_id
    import aws_sdk_bcm_pricing_calculator.types.service_code
    import aws_sdk_bcm_pricing_calculator.types.usage_group
    import aws_sdk_bcm_pricing_calculator.types.usage_type
    import aws_sdk_bcm_pricing_calculator.types.workload_estimate_cost_status
    import aws_sdk_bcm_pricing_calculator.types.workload_estimate_usage_quantity


class WorkloadEstimateUsageItem(TypedDict, closed=True):
    service_code: "aws_sdk_bcm_pricing_calculator.types.service_code.ServiceCode"
    """<p> The Amazon Web Services service code associated with this usage item. </p>"""
    usage_type: "aws_sdk_bcm_pricing_calculator.types.usage_type.UsageType"
    """<p> The type of usage for this item. </p>"""
    operation: "aws_sdk_bcm_pricing_calculator.types.operation.Operation"
    """<p> The specific operation associated with this usage item. </p>"""
    location: NotRequired["str"]
    """<p> The location associated with this usage item. </p>"""
    id: NotRequired["aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId"]
    """<p> The unique identifier of this usage item. </p>"""
    usage_account_id: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.account_id.AccountId"
    ]
    """<p> The Amazon Web Services account ID associated with this usage item. </p>"""
    group: NotRequired["aws_sdk_bcm_pricing_calculator.types.usage_group.UsageGroup"]
    """<p> The group identifier for this usage item. </p>"""
    quantity: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.workload_estimate_usage_quantity.WorkloadEstimateUsageQuantity"
    ]
    """<p> The estimated usage quantity for this item. </p>"""
    cost: NotRequired["float"]
    """<p> The estimated cost for this usage item. </p>"""
    currency: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.currency_code.CurrencyCode"
    ]
    """<p> The currency of the estimated cost. </p>"""
    status: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.workload_estimate_cost_status.WorkloadEstimateCostStatus"
    ]
    """<p> The current status of this usage item. </p>"""
    historical_usage: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.historical_usage_entity.HistoricalUsageEntity"
    ]
    """<p> Historical usage data associated with this item, if available. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkloadEstimateUsageItem) -> dict:
    out: dict = {}
    out["serviceCode"] = value["service_code"]
    out["usageType"] = value["usage_type"]
    out["operation"] = value["operation"]
    if "location" in value:
        out["location"] = value["location"]
    if "id" in value:
        out["id"] = value["id"]
    if "usage_account_id" in value:
        out["usageAccountId"] = value["usage_account_id"]
    if "group" in value:
        out["group"] = value["group"]
    if "quantity" in value:
        import aws_sdk_bcm_pricing_calculator.types.workload_estimate_usage_quantity

        out["quantity"] = (
            aws_sdk_bcm_pricing_calculator.types.workload_estimate_usage_quantity.serialize_aws_json_1_0(
                value["quantity"]
            )
        )
    if "cost" in value:
        out["cost"] = value["cost"]
    if "currency" in value:
        import aws_sdk_bcm_pricing_calculator.types.currency_code

        out["currency"] = (
            aws_sdk_bcm_pricing_calculator.types.currency_code.serialize_aws_json_1_0(
                value["currency"]
            )
        )
    if "status" in value:
        import aws_sdk_bcm_pricing_calculator.types.workload_estimate_cost_status

        out["status"] = (
            aws_sdk_bcm_pricing_calculator.types.workload_estimate_cost_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "historical_usage" in value:
        import aws_sdk_bcm_pricing_calculator.types.historical_usage_entity

        out["historicalUsage"] = (
            aws_sdk_bcm_pricing_calculator.types.historical_usage_entity.serialize_aws_json_1_0(
                value["historical_usage"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkloadEstimateUsageItem:
    out: WorkloadEstimateUsageItem = {}  # type: ignore[typeddict-item]
    if "serviceCode" in data:
        out["service_code"] = data["serviceCode"]
    else:
        raise DeserializationError("WorkloadEstimateUsageItem.service_code required")
    if "usageType" in data:
        out["usage_type"] = data["usageType"]
    else:
        raise DeserializationError("WorkloadEstimateUsageItem.usage_type required")
    if "operation" in data:
        out["operation"] = data["operation"]
    else:
        raise DeserializationError("WorkloadEstimateUsageItem.operation required")
    if "location" in data:
        out["location"] = data["location"]
    if "id" in data:
        out["id"] = data["id"]
    if "usageAccountId" in data:
        out["usage_account_id"] = data["usageAccountId"]
    if "group" in data:
        out["group"] = data["group"]
    if "quantity" in data:
        import aws_sdk_bcm_pricing_calculator.types.workload_estimate_usage_quantity

        out["quantity"] = (
            aws_sdk_bcm_pricing_calculator.types.workload_estimate_usage_quantity.deserialize_aws_json_1_0(
                data["quantity"]
            )
        )
    if "cost" in data:
        out["cost"] = data["cost"]
    if "currency" in data:
        import aws_sdk_bcm_pricing_calculator.types.currency_code

        out["currency"] = (
            aws_sdk_bcm_pricing_calculator.types.currency_code.deserialize_aws_json_1_0(
                data["currency"]
            )
        )
    if "status" in data:
        import aws_sdk_bcm_pricing_calculator.types.workload_estimate_cost_status

        out["status"] = (
            aws_sdk_bcm_pricing_calculator.types.workload_estimate_cost_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "historicalUsage" in data:
        import aws_sdk_bcm_pricing_calculator.types.historical_usage_entity

        out["historical_usage"] = (
            aws_sdk_bcm_pricing_calculator.types.historical_usage_entity.deserialize_aws_json_1_0(
                data["historicalUsage"]
            )
        )
    return out
