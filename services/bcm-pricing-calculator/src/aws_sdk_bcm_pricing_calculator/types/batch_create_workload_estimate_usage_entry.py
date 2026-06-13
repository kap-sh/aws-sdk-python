"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchCreateWorkloadEstimateUsageEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.account_id
    import aws_sdk_bcm_pricing_calculator.types.historical_usage_entity
    import aws_sdk_bcm_pricing_calculator.types.key
    import aws_sdk_bcm_pricing_calculator.types.operation
    import aws_sdk_bcm_pricing_calculator.types.service_code
    import aws_sdk_bcm_pricing_calculator.types.usage_group
    import aws_sdk_bcm_pricing_calculator.types.usage_type


class BatchCreateWorkloadEstimateUsageEntry(TypedDict):
    service_code: "aws_sdk_bcm_pricing_calculator.types.service_code.ServiceCode"
    """<p> The Amazon Web Services service code for this usage estimate. </p>"""
    usage_type: "aws_sdk_bcm_pricing_calculator.types.usage_type.UsageType"
    """<p> The type of usage being estimated. </p>"""
    operation: "aws_sdk_bcm_pricing_calculator.types.operation.Operation"
    """<p> The specific operation associated with this usage estimate. </p>"""
    key: "aws_sdk_bcm_pricing_calculator.types.key.Key"
    """<p> A unique identifier for this entry in the batch operation. </p>"""
    group: NotRequired["aws_sdk_bcm_pricing_calculator.types.usage_group.UsageGroup"]
    """<p> An optional group identifier for the usage estimate. </p>"""
    usage_account_id: "aws_sdk_bcm_pricing_calculator.types.account_id.AccountId"
    """<p> The Amazon Web Services account ID associated with this usage estimate. </p>"""
    amount: "float"
    """<p> The estimated usage amount. </p>"""
    historical_usage: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.historical_usage_entity.HistoricalUsageEntity"
    ]
    """<p> Historical usage data associated with this estimate, if available. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchCreateWorkloadEstimateUsageEntry) -> dict:
    out: dict = {}
    out["serviceCode"] = value["service_code"]
    out["usageType"] = value["usage_type"]
    out["operation"] = value["operation"]
    out["key"] = value["key"]
    if "group" in value:
        out["group"] = value["group"]
    out["usageAccountId"] = value["usage_account_id"]
    out["amount"] = value["amount"]
    if "historical_usage" in value:
        import aws_sdk_bcm_pricing_calculator.types.historical_usage_entity

        out["historicalUsage"] = (
            aws_sdk_bcm_pricing_calculator.types.historical_usage_entity.serialize_aws_json_1_0(
                value["historical_usage"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchCreateWorkloadEstimateUsageEntry:
    out: BatchCreateWorkloadEstimateUsageEntry = {}  # type: ignore[typeddict-item]
    if "serviceCode" in data:
        out["service_code"] = data["serviceCode"]
    else:
        raise DeserializationError(
            "BatchCreateWorkloadEstimateUsageEntry.service_code required"
        )
    if "usageType" in data:
        out["usage_type"] = data["usageType"]
    else:
        raise DeserializationError(
            "BatchCreateWorkloadEstimateUsageEntry.usage_type required"
        )
    if "operation" in data:
        out["operation"] = data["operation"]
    else:
        raise DeserializationError(
            "BatchCreateWorkloadEstimateUsageEntry.operation required"
        )
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("BatchCreateWorkloadEstimateUsageEntry.key required")
    if "group" in data:
        out["group"] = data["group"]
    if "usageAccountId" in data:
        out["usage_account_id"] = data["usageAccountId"]
    else:
        raise DeserializationError(
            "BatchCreateWorkloadEstimateUsageEntry.usage_account_id required"
        )
    if "amount" in data:
        out["amount"] = data["amount"]
    else:
        raise DeserializationError(
            "BatchCreateWorkloadEstimateUsageEntry.amount required"
        )
    if "historicalUsage" in data:
        import aws_sdk_bcm_pricing_calculator.types.historical_usage_entity

        out["historical_usage"] = (
            aws_sdk_bcm_pricing_calculator.types.historical_usage_entity.deserialize_aws_json_1_0(
                data["historicalUsage"]
            )
        )
    return out
