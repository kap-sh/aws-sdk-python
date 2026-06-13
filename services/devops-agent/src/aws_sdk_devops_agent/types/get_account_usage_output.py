"""Generated from Smithy shape ``com.amazonaws.devopsagent#GetAccountUsageOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.date_time
    import aws_sdk_devops_agent.types.usage_metric


class GetAccountUsageOutput(TypedDict):
    monthly_account_investigation_hours: NotRequired[
        "aws_sdk_devops_agent.types.usage_metric.UsageMetric"
    ]
    """<p>Monthly investigation hours usage and limit for an account</p>"""
    monthly_account_evaluation_hours: NotRequired[
        "aws_sdk_devops_agent.types.usage_metric.UsageMetric"
    ]
    """<p>Monthly evaluation hours usage and limit for an account</p>"""
    monthly_account_system_learning_hours: NotRequired[
        "aws_sdk_devops_agent.types.usage_metric.UsageMetric"
    ]
    """<p>Monthly system learning hours usage and limit for an account</p>"""
    monthly_account_on_demand_hours: NotRequired[
        "aws_sdk_devops_agent.types.usage_metric.UsageMetric"
    ]
    """<p>Monthly on-demand hours usage and limit for an account</p>"""
    usage_period_start_time: "aws_sdk_devops_agent.types.date_time.DateTime"
    """<p>The start time of the usage tracking period</p>"""
    usage_period_end_time: "aws_sdk_devops_agent.types.date_time.DateTime"
    """<p>The end time of the usage tracking period</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccountUsageOutput) -> dict:
    out: dict = {}
    if "monthly_account_investigation_hours" in value:
        import aws_sdk_devops_agent.types.usage_metric

        out["monthlyAccountInvestigationHours"] = (
            aws_sdk_devops_agent.types.usage_metric.serialize_json(
                value["monthly_account_investigation_hours"]
            )
        )
    if "monthly_account_evaluation_hours" in value:
        import aws_sdk_devops_agent.types.usage_metric

        out["monthlyAccountEvaluationHours"] = (
            aws_sdk_devops_agent.types.usage_metric.serialize_json(
                value["monthly_account_evaluation_hours"]
            )
        )
    if "monthly_account_system_learning_hours" in value:
        import aws_sdk_devops_agent.types.usage_metric

        out["monthlyAccountSystemLearningHours"] = (
            aws_sdk_devops_agent.types.usage_metric.serialize_json(
                value["monthly_account_system_learning_hours"]
            )
        )
    if "monthly_account_on_demand_hours" in value:
        import aws_sdk_devops_agent.types.usage_metric

        out["monthlyAccountOnDemandHours"] = (
            aws_sdk_devops_agent.types.usage_metric.serialize_json(
                value["monthly_account_on_demand_hours"]
            )
        )
    import aws_sdk_devops_agent.types.date_time

    out["usagePeriodStartTime"] = aws_sdk_devops_agent.types.date_time.serialize_json(
        value["usage_period_start_time"]
    )
    import aws_sdk_devops_agent.types.date_time

    out["usagePeriodEndTime"] = aws_sdk_devops_agent.types.date_time.serialize_json(
        value["usage_period_end_time"]
    )
    return out


def deserialize_json(data: dict) -> GetAccountUsageOutput:
    out: GetAccountUsageOutput = {}  # type: ignore[typeddict-item]
    if "monthlyAccountInvestigationHours" in data:
        import aws_sdk_devops_agent.types.usage_metric

        out["monthly_account_investigation_hours"] = (
            aws_sdk_devops_agent.types.usage_metric.deserialize_json(
                data["monthlyAccountInvestigationHours"]
            )
        )
    if "monthlyAccountEvaluationHours" in data:
        import aws_sdk_devops_agent.types.usage_metric

        out["monthly_account_evaluation_hours"] = (
            aws_sdk_devops_agent.types.usage_metric.deserialize_json(
                data["monthlyAccountEvaluationHours"]
            )
        )
    if "monthlyAccountSystemLearningHours" in data:
        import aws_sdk_devops_agent.types.usage_metric

        out["monthly_account_system_learning_hours"] = (
            aws_sdk_devops_agent.types.usage_metric.deserialize_json(
                data["monthlyAccountSystemLearningHours"]
            )
        )
    if "monthlyAccountOnDemandHours" in data:
        import aws_sdk_devops_agent.types.usage_metric

        out["monthly_account_on_demand_hours"] = (
            aws_sdk_devops_agent.types.usage_metric.deserialize_json(
                data["monthlyAccountOnDemandHours"]
            )
        )
    if "usagePeriodStartTime" in data:
        import aws_sdk_devops_agent.types.date_time

        out["usage_period_start_time"] = (
            aws_sdk_devops_agent.types.date_time.deserialize_json(
                data["usagePeriodStartTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetAccountUsageOutput.usage_period_start_time required"
        )
    if "usagePeriodEndTime" in data:
        import aws_sdk_devops_agent.types.date_time

        out["usage_period_end_time"] = (
            aws_sdk_devops_agent.types.date_time.deserialize_json(
                data["usagePeriodEndTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetAccountUsageOutput.usage_period_end_time required"
        )
    return out
