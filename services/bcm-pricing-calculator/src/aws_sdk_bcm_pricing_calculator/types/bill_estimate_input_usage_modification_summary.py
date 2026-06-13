"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BillEstimateInputUsageModificationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.account_id
    import aws_sdk_bcm_pricing_calculator.types.availability_zone
    import aws_sdk_bcm_pricing_calculator.types.historical_usage_entity
    import aws_sdk_bcm_pricing_calculator.types.operation
    import aws_sdk_bcm_pricing_calculator.types.resource_id
    import aws_sdk_bcm_pricing_calculator.types.service_code
    import aws_sdk_bcm_pricing_calculator.types.usage_group
    import aws_sdk_bcm_pricing_calculator.types.usage_quantities
    import aws_sdk_bcm_pricing_calculator.types.usage_type


class BillEstimateInputUsageModificationSummary(TypedDict):
    service_code: "aws_sdk_bcm_pricing_calculator.types.service_code.ServiceCode"
    """<p> The Amazon Web Services service code for this usage modification. </p>"""
    usage_type: "aws_sdk_bcm_pricing_calculator.types.usage_type.UsageType"
    """<p> The type of usage being modified. </p>"""
    operation: "aws_sdk_bcm_pricing_calculator.types.operation.Operation"
    """<p> The specific operation associated with this usage modification. </p>"""
    location: NotRequired["str"]
    """<p> The location associated with this usage modification. </p>"""
    availability_zone: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.availability_zone.AvailabilityZone"
    ]
    """<p> The availability zone associated with this usage modification, if applicable. </p>"""
    id: NotRequired["aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId"]
    """<p> The unique identifier of the usage modification. </p>"""
    group: NotRequired["aws_sdk_bcm_pricing_calculator.types.usage_group.UsageGroup"]
    """<p> The group identifier for the usage modification. </p>"""
    usage_account_id: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.account_id.AccountId"
    ]
    """<p> The Amazon Web Services account ID associated with this usage modification. </p>"""
    quantities: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.usage_quantities.UsageQuantities"
    ]
    """<p> The modified usage quantities. </p>"""
    historical_usage: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.historical_usage_entity.HistoricalUsageEntity"
    ]
    """<p> Historical usage data associated with this modification, if available. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillEstimateInputUsageModificationSummary) -> dict:
    out: dict = {}
    out["serviceCode"] = value["service_code"]
    out["usageType"] = value["usage_type"]
    out["operation"] = value["operation"]
    if "location" in value:
        out["location"] = value["location"]
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "id" in value:
        out["id"] = value["id"]
    if "group" in value:
        out["group"] = value["group"]
    if "usage_account_id" in value:
        out["usageAccountId"] = value["usage_account_id"]
    if "quantities" in value:
        import aws_sdk_bcm_pricing_calculator.types.usage_quantities

        out["quantities"] = (
            aws_sdk_bcm_pricing_calculator.types.usage_quantities.serialize_aws_json_1_0(
                value["quantities"]
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


def deserialize_aws_json_1_0(data: dict) -> BillEstimateInputUsageModificationSummary:
    out: BillEstimateInputUsageModificationSummary = {}  # type: ignore[typeddict-item]
    if "serviceCode" in data:
        out["service_code"] = data["serviceCode"]
    else:
        raise DeserializationError(
            "BillEstimateInputUsageModificationSummary.service_code required"
        )
    if "usageType" in data:
        out["usage_type"] = data["usageType"]
    else:
        raise DeserializationError(
            "BillEstimateInputUsageModificationSummary.usage_type required"
        )
    if "operation" in data:
        out["operation"] = data["operation"]
    else:
        raise DeserializationError(
            "BillEstimateInputUsageModificationSummary.operation required"
        )
    if "location" in data:
        out["location"] = data["location"]
    if "availabilityZone" in data:
        out["availability_zone"] = data["availabilityZone"]
    if "id" in data:
        out["id"] = data["id"]
    if "group" in data:
        out["group"] = data["group"]
    if "usageAccountId" in data:
        out["usage_account_id"] = data["usageAccountId"]
    if "quantities" in data:
        import aws_sdk_bcm_pricing_calculator.types.usage_quantities

        out["quantities"] = (
            aws_sdk_bcm_pricing_calculator.types.usage_quantities.deserialize_aws_json_1_0(
                data["quantities"]
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
