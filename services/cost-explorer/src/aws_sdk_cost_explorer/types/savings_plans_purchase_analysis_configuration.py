"""Generated from Smithy shape ``com.amazonaws.costexplorer#SavingsPlansPurchaseAnalysisConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.account_id
    import aws_sdk_cost_explorer.types.account_scope
    import aws_sdk_cost_explorer.types.analysis_type
    import aws_sdk_cost_explorer.types.date_interval
    import aws_sdk_cost_explorer.types.savings_plans_target_coverage
    import aws_sdk_cost_explorer.types.savings_plans_to_add
    import aws_sdk_cost_explorer.types.savings_plans_to_exclude


class SavingsPlansPurchaseAnalysisConfiguration(TypedDict):
    account_scope: NotRequired["aws_sdk_cost_explorer.types.account_scope.AccountScope"]
    """<p>The account scope that you want your analysis for.</p>"""
    account_id: NotRequired["aws_sdk_cost_explorer.types.account_id.AccountId"]
    """<p>The account that the analysis is for.</p>"""
    analysis_type: "aws_sdk_cost_explorer.types.analysis_type.AnalysisType"
    """<p>The type of analysis.</p>"""
    savings_plans_to_add: (
        "aws_sdk_cost_explorer.types.savings_plans_to_add.SavingsPlansToAdd"
    )
    """<p>Savings Plans to include in the analysis.</p>"""
    savings_plans_to_exclude: NotRequired[
        "aws_sdk_cost_explorer.types.savings_plans_to_exclude.SavingsPlansToExclude"
    ]
    """<p>Savings Plans to exclude from the analysis.</p>"""
    look_back_time_period: "aws_sdk_cost_explorer.types.date_interval.DateInterval"
    """<p>The time period associated with the analysis.</p>"""
    savings_plans_target_coverage: NotRequired[
        "aws_sdk_cost_explorer.types.savings_plans_target_coverage.SavingsPlansTargetCoverage"
    ]
    """<p>Specifies the target Savings Plans coverage as a percentage from <code>10</code> to <code>100</code>. This field is required when <code>AnalysisType</code> is <code>TARGET_AVERAGE_COVERAGE</code>. It defines the target average hourly coverage that the recommended Savings Plans commitment should achieve over the lookback period.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SavingsPlansPurchaseAnalysisConfiguration) -> dict:
    out: dict = {}
    if "account_scope" in value:
        import aws_sdk_cost_explorer.types.account_scope

        out["AccountScope"] = (
            aws_sdk_cost_explorer.types.account_scope.serialize_aws_json_1_1(
                value["account_scope"]
            )
        )
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    import aws_sdk_cost_explorer.types.analysis_type

    out["AnalysisType"] = (
        aws_sdk_cost_explorer.types.analysis_type.serialize_aws_json_1_1(
            value["analysis_type"]
        )
    )
    import aws_sdk_cost_explorer.types.savings_plans_to_add

    out["SavingsPlansToAdd"] = (
        aws_sdk_cost_explorer.types.savings_plans_to_add.serialize_aws_json_1_1(
            value["savings_plans_to_add"]
        )
    )
    if "savings_plans_to_exclude" in value:
        import aws_sdk_cost_explorer.types.savings_plans_to_exclude

        out["SavingsPlansToExclude"] = (
            aws_sdk_cost_explorer.types.savings_plans_to_exclude.serialize_aws_json_1_1(
                value["savings_plans_to_exclude"]
            )
        )
    import aws_sdk_cost_explorer.types.date_interval

    out["LookBackTimePeriod"] = (
        aws_sdk_cost_explorer.types.date_interval.serialize_aws_json_1_1(
            value["look_back_time_period"]
        )
    )
    if "savings_plans_target_coverage" in value:
        out["SavingsPlansTargetCoverage"] = value["savings_plans_target_coverage"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SavingsPlansPurchaseAnalysisConfiguration:
    out: SavingsPlansPurchaseAnalysisConfiguration = {}  # type: ignore[typeddict-item]
    if "AccountScope" in data:
        import aws_sdk_cost_explorer.types.account_scope

        out["account_scope"] = (
            aws_sdk_cost_explorer.types.account_scope.deserialize_aws_json_1_1(
                data["AccountScope"]
            )
        )
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "AnalysisType" in data:
        import aws_sdk_cost_explorer.types.analysis_type

        out["analysis_type"] = (
            aws_sdk_cost_explorer.types.analysis_type.deserialize_aws_json_1_1(
                data["AnalysisType"]
            )
        )
    else:
        raise DeserializationError(
            "SavingsPlansPurchaseAnalysisConfiguration.analysis_type required"
        )
    if "SavingsPlansToAdd" in data:
        import aws_sdk_cost_explorer.types.savings_plans_to_add

        out["savings_plans_to_add"] = (
            aws_sdk_cost_explorer.types.savings_plans_to_add.deserialize_aws_json_1_1(
                data["SavingsPlansToAdd"]
            )
        )
    else:
        raise DeserializationError(
            "SavingsPlansPurchaseAnalysisConfiguration.savings_plans_to_add required"
        )
    if "SavingsPlansToExclude" in data:
        import aws_sdk_cost_explorer.types.savings_plans_to_exclude

        out["savings_plans_to_exclude"] = (
            aws_sdk_cost_explorer.types.savings_plans_to_exclude.deserialize_aws_json_1_1(
                data["SavingsPlansToExclude"]
            )
        )
    if "LookBackTimePeriod" in data:
        import aws_sdk_cost_explorer.types.date_interval

        out["look_back_time_period"] = (
            aws_sdk_cost_explorer.types.date_interval.deserialize_aws_json_1_1(
                data["LookBackTimePeriod"]
            )
        )
    else:
        raise DeserializationError(
            "SavingsPlansPurchaseAnalysisConfiguration.look_back_time_period required"
        )
    if "SavingsPlansTargetCoverage" in data:
        out["savings_plans_target_coverage"] = data["SavingsPlansTargetCoverage"]
    return out
