"""Generated from Smithy shape ``com.amazonaws.freetier#FreeTierUsage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_freetier.types.generic_double
    import aws_sdk_freetier.types.generic_string


class FreeTierUsage(TypedDict):
    service: NotRequired["aws_sdk_freetier.types.generic_string.GenericString"]
    """<p>The name of the Amazon Web Services service providing the Free Tier offer. For example, this can be Amazon Elastic Compute Cloud.</p>"""
    operation: NotRequired["aws_sdk_freetier.types.generic_string.GenericString"]
    """<p>Describes <code>usageType</code> more granularly with the specific Amazon Web Services service API operation. For example, this can be the <code>RunInstances</code> API operation for Amazon Elastic Compute Cloud.</p>"""
    usage_type: NotRequired["aws_sdk_freetier.types.generic_string.GenericString"]
    """<p>Describes the usage details of the offer. For example, this might be <code>Global-BoxUsage:freetrial</code>.</p>"""
    region: NotRequired["aws_sdk_freetier.types.generic_string.GenericString"]
    """<p>Describes the Amazon Web Services Region for which this offer is applicable</p>"""
    actual_usage_amount: "aws_sdk_freetier.types.generic_double.GenericDouble"
    """<p>Describes the actual usage accrued month-to-day (MTD) that you've used so far.</p>"""
    forecasted_usage_amount: "aws_sdk_freetier.types.generic_double.GenericDouble"
    """<p>Describes the forecasted usage by the month that you're expected to use.</p>"""
    limit: "aws_sdk_freetier.types.generic_double.GenericDouble"
    """<p>Describes the maximum usage allowed in Free Tier.</p>"""
    unit: NotRequired["aws_sdk_freetier.types.generic_string.GenericString"]
    """<p>Describes the unit of the <code>usageType</code>, such as <code>Hrs</code>.</p>"""
    description: NotRequired["aws_sdk_freetier.types.generic_string.GenericString"]
    """<p>The description of the Free Tier offer.</p>"""
    free_tier_type: NotRequired["aws_sdk_freetier.types.generic_string.GenericString"]
    """<p>Describes the type of the Free Tier offer. For example, the offer can be <code>\"12 Months Free\"</code>, <code>\"Always Free\"</code>, and <code>\"Free Trial\"</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FreeTierUsage) -> dict:
    out: dict = {}
    if "service" in value:
        out["service"] = value["service"]
    if "operation" in value:
        out["operation"] = value["operation"]
    if "usage_type" in value:
        out["usageType"] = value["usage_type"]
    if "region" in value:
        out["region"] = value["region"]
    out["actualUsageAmount"] = value.get("actual_usage_amount", 0)
    out["forecastedUsageAmount"] = value.get("forecasted_usage_amount", 0)
    out["limit"] = value.get("limit", 0)
    if "unit" in value:
        out["unit"] = value["unit"]
    if "description" in value:
        out["description"] = value["description"]
    if "free_tier_type" in value:
        out["freeTierType"] = value["free_tier_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> FreeTierUsage:
    out: FreeTierUsage = {}  # type: ignore[typeddict-item]
    if "service" in data:
        out["service"] = data["service"]
    if "operation" in data:
        out["operation"] = data["operation"]
    if "usageType" in data:
        out["usage_type"] = data["usageType"]
    if "region" in data:
        out["region"] = data["region"]
    if "actualUsageAmount" in data:
        out["actual_usage_amount"] = data["actualUsageAmount"]
    else:
        out["actual_usage_amount"] = 0
    if "forecastedUsageAmount" in data:
        out["forecasted_usage_amount"] = data["forecastedUsageAmount"]
    else:
        out["forecasted_usage_amount"] = 0
    if "limit" in data:
        out["limit"] = data["limit"]
    else:
        out["limit"] = 0
    if "unit" in data:
        out["unit"] = data["unit"]
    if "description" in data:
        out["description"] = data["description"]
    if "freeTierType" in data:
        out["free_tier_type"] = data["freeTierType"]
    return out
