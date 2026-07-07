"""Generated from Smithy shape ``com.amazonaws.costexplorer#SavingsPlansCoverage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.attributes
    import aws_sdk_cost_explorer.types.date_interval
    import aws_sdk_cost_explorer.types.savings_plans_coverage_data


class SavingsPlansCoverage(TypedDict, closed=True):
    attributes: NotRequired["aws_sdk_cost_explorer.types.attributes.Attributes"]
    """<p>The attribute that applies to a specific <code>Dimension</code>.</p>"""
    coverage: NotRequired[
        "aws_sdk_cost_explorer.types.savings_plans_coverage_data.SavingsPlansCoverageData"
    ]
    """<p>The amount of Savings Plans eligible usage that the Savings Plans covered.</p>"""
    time_period: NotRequired["aws_sdk_cost_explorer.types.date_interval.DateInterval"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SavingsPlansCoverage) -> dict:
    out: dict = {}
    if "attributes" in value:
        import aws_sdk_cost_explorer.types.attributes

        out["Attributes"] = (
            aws_sdk_cost_explorer.types.attributes.serialize_aws_json_1_1(
                value["attributes"]
            )
        )
    if "coverage" in value:
        import aws_sdk_cost_explorer.types.savings_plans_coverage_data

        out["Coverage"] = (
            aws_sdk_cost_explorer.types.savings_plans_coverage_data.serialize_aws_json_1_1(
                value["coverage"]
            )
        )
    if "time_period" in value:
        import aws_sdk_cost_explorer.types.date_interval

        out["TimePeriod"] = (
            aws_sdk_cost_explorer.types.date_interval.serialize_aws_json_1_1(
                value["time_period"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SavingsPlansCoverage:
    out: SavingsPlansCoverage = {}  # type: ignore[typeddict-item]
    if "Attributes" in data:
        import aws_sdk_cost_explorer.types.attributes

        out["attributes"] = (
            aws_sdk_cost_explorer.types.attributes.deserialize_aws_json_1_1(
                data["Attributes"]
            )
        )
    if "Coverage" in data:
        import aws_sdk_cost_explorer.types.savings_plans_coverage_data

        out["coverage"] = (
            aws_sdk_cost_explorer.types.savings_plans_coverage_data.deserialize_aws_json_1_1(
                data["Coverage"]
            )
        )
    if "TimePeriod" in data:
        import aws_sdk_cost_explorer.types.date_interval

        out["time_period"] = (
            aws_sdk_cost_explorer.types.date_interval.deserialize_aws_json_1_1(
                data["TimePeriod"]
            )
        )
    return out
