"""Generated from Smithy shape ``com.amazonaws.costexplorer#TargetInstance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.generic_boolean
    import capo_cost_explorer.types.generic_string
    import capo_cost_explorer.types.platform_differences
    import capo_cost_explorer.types.resource_details
    import capo_cost_explorer.types.resource_utilization


class TargetInstance(TypedDict, closed=True):
    estimated_monthly_cost: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The expected cost to operate this instance type on a monthly basis.</p>"""
    estimated_monthly_savings: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The estimated savings that result from modification, on a monthly basis.</p>"""
    currency_code: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>The currency code that Amazon Web Services used to calculate the costs for this instance.</p>"""
    default_target_instance: "capo_cost_explorer.types.generic_boolean.GenericBoolean"
    """<p>Determines whether this recommendation is the defaulted Amazon Web Services recommendation.</p>"""
    resource_details: NotRequired[
        "capo_cost_explorer.types.resource_details.ResourceDetails"
    ]
    """<p>Details on the target instance type. </p>"""
    expected_resource_utilization: NotRequired[
        "capo_cost_explorer.types.resource_utilization.ResourceUtilization"
    ]
    """<p>The expected utilization metrics for target instance type.</p>"""
    platform_differences: NotRequired[
        "capo_cost_explorer.types.platform_differences.PlatformDifferences"
    ]
    """<p>Explains the actions that you might need to take to successfully migrate your workloads from the current instance type to the recommended instance type. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetInstance) -> dict:
    out: dict = {}
    if "estimated_monthly_cost" in value:
        out["EstimatedMonthlyCost"] = value["estimated_monthly_cost"]
    if "estimated_monthly_savings" in value:
        out["EstimatedMonthlySavings"] = value["estimated_monthly_savings"]
    if "currency_code" in value:
        out["CurrencyCode"] = value["currency_code"]
    out["DefaultTargetInstance"] = value.get("default_target_instance", False)
    if "resource_details" in value:
        import capo_cost_explorer.types.resource_details

        out["ResourceDetails"] = (
            capo_cost_explorer.types.resource_details.serialize_aws_json_1_1(
                value["resource_details"]
            )
        )
    if "expected_resource_utilization" in value:
        import capo_cost_explorer.types.resource_utilization

        out["ExpectedResourceUtilization"] = (
            capo_cost_explorer.types.resource_utilization.serialize_aws_json_1_1(
                value["expected_resource_utilization"]
            )
        )
    if "platform_differences" in value:
        import capo_cost_explorer.types.platform_differences

        out["PlatformDifferences"] = (
            capo_cost_explorer.types.platform_differences.serialize_aws_json_1_1(
                value["platform_differences"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetInstance:
    out: TargetInstance = {}  # type: ignore[typeddict-item]
    if "EstimatedMonthlyCost" in data:
        out["estimated_monthly_cost"] = data["EstimatedMonthlyCost"]
    if "EstimatedMonthlySavings" in data:
        out["estimated_monthly_savings"] = data["EstimatedMonthlySavings"]
    if "CurrencyCode" in data:
        out["currency_code"] = data["CurrencyCode"]
    if "DefaultTargetInstance" in data:
        out["default_target_instance"] = data["DefaultTargetInstance"]
    else:
        out["default_target_instance"] = False
    if "ResourceDetails" in data:
        import capo_cost_explorer.types.resource_details

        out["resource_details"] = (
            capo_cost_explorer.types.resource_details.deserialize_aws_json_1_1(
                data["ResourceDetails"]
            )
        )
    if "ExpectedResourceUtilization" in data:
        import capo_cost_explorer.types.resource_utilization

        out["expected_resource_utilization"] = (
            capo_cost_explorer.types.resource_utilization.deserialize_aws_json_1_1(
                data["ExpectedResourceUtilization"]
            )
        )
    if "PlatformDifferences" in data:
        import capo_cost_explorer.types.platform_differences

        out["platform_differences"] = (
            capo_cost_explorer.types.platform_differences.deserialize_aws_json_1_1(
                data["PlatformDifferences"]
            )
        )
    return out
