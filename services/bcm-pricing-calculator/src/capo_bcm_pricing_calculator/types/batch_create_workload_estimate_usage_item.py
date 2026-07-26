"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchCreateWorkloadEstimateUsageItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.account_id
    import capo_bcm_pricing_calculator.types.currency_code
    import capo_bcm_pricing_calculator.types.historical_usage_entity
    import capo_bcm_pricing_calculator.types.key
    import capo_bcm_pricing_calculator.types.operation
    import capo_bcm_pricing_calculator.types.resource_id
    import capo_bcm_pricing_calculator.types.service_code
    import capo_bcm_pricing_calculator.types.usage_group
    import capo_bcm_pricing_calculator.types.usage_type
    import capo_bcm_pricing_calculator.types.workload_estimate_cost_status
    import capo_bcm_pricing_calculator.types.workload_estimate_usage_quantity


class BatchCreateWorkloadEstimateUsageItem(TypedDict, closed=True):
    service_code: "capo_bcm_pricing_calculator.types.service_code.ServiceCode"
    """<p> The Amazon Web Services service code for this usage estimate. </p>"""
    usage_type: "capo_bcm_pricing_calculator.types.usage_type.UsageType"
    """<p> The type of usage that was estimated. </p>"""
    operation: "capo_bcm_pricing_calculator.types.operation.Operation"
    """<p> The specific operation associated with this usage estimate. </p>"""
    location: NotRequired["str"]
    """<p> The location associated with this usage estimate. </p>"""
    id: NotRequired["capo_bcm_pricing_calculator.types.resource_id.ResourceId"]
    """<p> The unique identifier assigned to the created usage estimate. </p>"""
    usage_account_id: NotRequired[
        "capo_bcm_pricing_calculator.types.account_id.AccountId"
    ]
    """<p> The Amazon Web Services account ID associated with the created usage estimate. </p>"""
    group: NotRequired["capo_bcm_pricing_calculator.types.usage_group.UsageGroup"]
    """<p> The group identifier for the created usage estimate. </p>"""
    quantity: NotRequired[
        "capo_bcm_pricing_calculator.types.workload_estimate_usage_quantity.WorkloadEstimateUsageQuantity"
    ]
    """<p> The estimated usage quantity. </p>"""
    cost: NotRequired["float"]
    """<p> The estimated cost associated with this usage. </p>"""
    currency: NotRequired[
        "capo_bcm_pricing_calculator.types.currency_code.CurrencyCode"
    ]
    """<p> The currency of the estimated cost. </p>"""
    status: NotRequired[
        "capo_bcm_pricing_calculator.types.workload_estimate_cost_status.WorkloadEstimateCostStatus"
    ]
    """<p> The current status of the created usage estimate. </p>"""
    historical_usage: NotRequired[
        "capo_bcm_pricing_calculator.types.historical_usage_entity.HistoricalUsageEntity"
    ]
    """<p> Historical usage data associated with this estimate, if available. </p>"""
    key: NotRequired["capo_bcm_pricing_calculator.types.key.Key"]
    """<p> The key of the successfully created entry. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchCreateWorkloadEstimateUsageItem) -> dict:
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
        import capo_bcm_pricing_calculator.types.workload_estimate_usage_quantity

        out["quantity"] = (
            capo_bcm_pricing_calculator.types.workload_estimate_usage_quantity.serialize_aws_json_1_0(
                value["quantity"]
            )
        )
    if "cost" in value:
        out["cost"] = value["cost"]
    if "currency" in value:
        import capo_bcm_pricing_calculator.types.currency_code

        out["currency"] = (
            capo_bcm_pricing_calculator.types.currency_code.serialize_aws_json_1_0(
                value["currency"]
            )
        )
    if "status" in value:
        import capo_bcm_pricing_calculator.types.workload_estimate_cost_status

        out["status"] = (
            capo_bcm_pricing_calculator.types.workload_estimate_cost_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "historical_usage" in value:
        import capo_bcm_pricing_calculator.types.historical_usage_entity

        out["historicalUsage"] = (
            capo_bcm_pricing_calculator.types.historical_usage_entity.serialize_aws_json_1_0(
                value["historical_usage"]
            )
        )
    if "key" in value:
        out["key"] = value["key"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchCreateWorkloadEstimateUsageItem:
    out: BatchCreateWorkloadEstimateUsageItem = {}  # type: ignore[typeddict-item]
    if "serviceCode" in data:
        out["service_code"] = data["serviceCode"]
    else:
        raise DeserializationError(
            "BatchCreateWorkloadEstimateUsageItem.service_code required"
        )
    if "usageType" in data:
        out["usage_type"] = data["usageType"]
    else:
        raise DeserializationError(
            "BatchCreateWorkloadEstimateUsageItem.usage_type required"
        )
    if "operation" in data:
        out["operation"] = data["operation"]
    else:
        raise DeserializationError(
            "BatchCreateWorkloadEstimateUsageItem.operation required"
        )
    if "location" in data:
        out["location"] = data["location"]
    if "id" in data:
        out["id"] = data["id"]
    if "usageAccountId" in data:
        out["usage_account_id"] = data["usageAccountId"]
    if "group" in data:
        out["group"] = data["group"]
    if "quantity" in data:
        import capo_bcm_pricing_calculator.types.workload_estimate_usage_quantity

        out["quantity"] = (
            capo_bcm_pricing_calculator.types.workload_estimate_usage_quantity.deserialize_aws_json_1_0(
                data["quantity"]
            )
        )
    if "cost" in data:
        out["cost"] = data["cost"]
    if "currency" in data:
        import capo_bcm_pricing_calculator.types.currency_code

        out["currency"] = (
            capo_bcm_pricing_calculator.types.currency_code.deserialize_aws_json_1_0(
                data["currency"]
            )
        )
    if "status" in data:
        import capo_bcm_pricing_calculator.types.workload_estimate_cost_status

        out["status"] = (
            capo_bcm_pricing_calculator.types.workload_estimate_cost_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "historicalUsage" in data:
        import capo_bcm_pricing_calculator.types.historical_usage_entity

        out["historical_usage"] = (
            capo_bcm_pricing_calculator.types.historical_usage_entity.deserialize_aws_json_1_0(
                data["historicalUsage"]
            )
        )
    if "key" in data:
        out["key"] = data["key"]
    return out
