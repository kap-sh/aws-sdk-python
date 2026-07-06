"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceLevelObjectiveBudgetReport``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.attainment
    import aws_sdk_application_signals.types.budget_requests_remaining
    import aws_sdk_application_signals.types.budget_seconds_remaining
    import aws_sdk_application_signals.types.evaluation_type
    import aws_sdk_application_signals.types.goal
    import aws_sdk_application_signals.types.request_based_service_level_indicator
    import aws_sdk_application_signals.types.service_level_indicator
    import aws_sdk_application_signals.types.service_level_objective_arn
    import aws_sdk_application_signals.types.service_level_objective_budget_status
    import aws_sdk_application_signals.types.service_level_objective_name
    import aws_sdk_application_signals.types.total_budget_requests
    import aws_sdk_application_signals.types.total_budget_seconds


class ServiceLevelObjectiveBudgetReport(TypedDict, closed=True):
    arn: "aws_sdk_application_signals.types.service_level_objective_arn.ServiceLevelObjectiveArn"
    """<p>The ARN of the SLO that this report is for.</p>"""
    name: "aws_sdk_application_signals.types.service_level_objective_name.ServiceLevelObjectiveName"
    """<p>The name of the SLO that this report is for.</p>"""
    evaluation_type: NotRequired[
        "aws_sdk_application_signals.types.evaluation_type.EvaluationType"
    ]
    """<p>Displays whether this budget report is for a period-based SLO or a request-based SLO.</p>"""
    budget_status: "aws_sdk_application_signals.types.service_level_objective_budget_status.ServiceLevelObjectiveBudgetStatus"
    """<p>The status of this SLO, as it relates to the error budget for the entire time interval.</p> <ul> <li> <p> <code>OK</code> means that the SLO had remaining budget above the warning threshold, as of the time that you specified in <code>TimeStamp</code>.</p> </li> <li> <p> <code>WARNING</code> means that the SLO's remaining budget was below the warning threshold, as of the time that you specified in <code>TimeStamp</code>.</p> </li> <li> <p> <code>BREACHED</code> means that the SLO's budget was exhausted, as of the time that you specified in <code>TimeStamp</code>.</p> </li> <li> <p> <code>INSUFFICIENT_DATA</code> means that the specified start and end times were before the SLO was created, or that attainment data is missing.</p> </li> </ul>"""
    attainment: NotRequired["aws_sdk_application_signals.types.attainment.Attainment"]
    """<p>A number between 0 and 100 that represents the success percentage of your application compared to the goal set by the SLO.</p> <p>If this is a period-based SLO, the number is the percentage of time periods that the service has attained the SLO's attainment goal, as of the time of the request.</p> <p>If this is a request-based SLO, the number is the number of successful requests divided by the number of total requests, multiplied by 100, during the time range that you specified in your request.</p>"""
    total_budget_seconds: NotRequired[
        "aws_sdk_application_signals.types.total_budget_seconds.TotalBudgetSeconds"
    ]
    """<p>The total number of seconds in the error budget for the interval. This field is included only if the SLO is a period-based SLO.</p>"""
    budget_seconds_remaining: NotRequired[
        "aws_sdk_application_signals.types.budget_seconds_remaining.BudgetSecondsRemaining"
    ]
    """<p>The budget amount remaining before the SLO status becomes <code>BREACHING</code>, at the time specified in the <code>Timestemp</code> parameter of the request. If this value is negative, then the SLO is already in <code>BREACHING</code> status.</p> <p> This field is included only if the SLO is a period-based SLO.</p>"""
    total_budget_requests: NotRequired[
        "aws_sdk_application_signals.types.total_budget_requests.TotalBudgetRequests"
    ]
    """<p>This field is displayed only for request-based SLOs. It displays the total number of failed requests that can be tolerated during the time range between the start of the interval and the time stamp supplied in the budget report request. It is based on the total number of requests that occurred, and the percentage specified in the attainment goal. If the number of failed requests matches this number or is higher, then this SLO is currently breaching.</p> <p>This number can go up and down between reports with different time stamps, based on both how many total requests occur.</p>"""
    budget_requests_remaining: NotRequired[
        "aws_sdk_application_signals.types.budget_requests_remaining.BudgetRequestsRemaining"
    ]
    """<p>This field is displayed only for request-based SLOs. It displays the number of failed requests that can be tolerated before any more successful requests occur, and still have the application meet its SLO goal.</p> <p>This number can go up and down between different reports, based on both how many successful requests and how many failed requests occur in that time.</p>"""
    sli: NotRequired[
        "aws_sdk_application_signals.types.service_level_indicator.ServiceLevelIndicator"
    ]
    """<p>A structure that contains information about the performance metric that this SLO monitors.</p>"""
    request_based_sli: NotRequired[
        "aws_sdk_application_signals.types.request_based_service_level_indicator.RequestBasedServiceLevelIndicator"
    ]
    goal: NotRequired["aws_sdk_application_signals.types.goal.Goal"]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceLevelObjectiveBudgetReport) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Name"] = value["name"]
    if "evaluation_type" in value:
        import aws_sdk_application_signals.types.evaluation_type

        out["EvaluationType"] = (
            aws_sdk_application_signals.types.evaluation_type.serialize_json(
                value["evaluation_type"]
            )
        )
    import aws_sdk_application_signals.types.service_level_objective_budget_status

    out["BudgetStatus"] = (
        aws_sdk_application_signals.types.service_level_objective_budget_status.serialize_json(
            value["budget_status"]
        )
    )
    if "attainment" in value:
        out["Attainment"] = value["attainment"]
    if "total_budget_seconds" in value:
        out["TotalBudgetSeconds"] = value["total_budget_seconds"]
    if "budget_seconds_remaining" in value:
        out["BudgetSecondsRemaining"] = value["budget_seconds_remaining"]
    if "total_budget_requests" in value:
        out["TotalBudgetRequests"] = value["total_budget_requests"]
    if "budget_requests_remaining" in value:
        out["BudgetRequestsRemaining"] = value["budget_requests_remaining"]
    if "sli" in value:
        import aws_sdk_application_signals.types.service_level_indicator

        out["Sli"] = (
            aws_sdk_application_signals.types.service_level_indicator.serialize_json(
                value["sli"]
            )
        )
    if "request_based_sli" in value:
        import aws_sdk_application_signals.types.request_based_service_level_indicator

        out["RequestBasedSli"] = (
            aws_sdk_application_signals.types.request_based_service_level_indicator.serialize_json(
                value["request_based_sli"]
            )
        )
    if "goal" in value:
        import aws_sdk_application_signals.types.goal

        out["Goal"] = aws_sdk_application_signals.types.goal.serialize_json(
            value["goal"]
        )
    return out


def deserialize_json(data: dict) -> ServiceLevelObjectiveBudgetReport:
    out: ServiceLevelObjectiveBudgetReport = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("ServiceLevelObjectiveBudgetReport.arn required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ServiceLevelObjectiveBudgetReport.name required")
    if "EvaluationType" in data:
        import aws_sdk_application_signals.types.evaluation_type

        out["evaluation_type"] = (
            aws_sdk_application_signals.types.evaluation_type.deserialize_json(
                data["EvaluationType"]
            )
        )
    if "BudgetStatus" in data:
        import aws_sdk_application_signals.types.service_level_objective_budget_status

        out["budget_status"] = (
            aws_sdk_application_signals.types.service_level_objective_budget_status.deserialize_json(
                data["BudgetStatus"]
            )
        )
    else:
        raise DeserializationError(
            "ServiceLevelObjectiveBudgetReport.budget_status required"
        )
    if "Attainment" in data:
        out["attainment"] = data["Attainment"]
    if "TotalBudgetSeconds" in data:
        out["total_budget_seconds"] = data["TotalBudgetSeconds"]
    if "BudgetSecondsRemaining" in data:
        out["budget_seconds_remaining"] = data["BudgetSecondsRemaining"]
    if "TotalBudgetRequests" in data:
        out["total_budget_requests"] = data["TotalBudgetRequests"]
    if "BudgetRequestsRemaining" in data:
        out["budget_requests_remaining"] = data["BudgetRequestsRemaining"]
    if "Sli" in data:
        import aws_sdk_application_signals.types.service_level_indicator

        out["sli"] = (
            aws_sdk_application_signals.types.service_level_indicator.deserialize_json(
                data["Sli"]
            )
        )
    if "RequestBasedSli" in data:
        import aws_sdk_application_signals.types.request_based_service_level_indicator

        out["request_based_sli"] = (
            aws_sdk_application_signals.types.request_based_service_level_indicator.deserialize_json(
                data["RequestBasedSli"]
            )
        )
    if "Goal" in data:
        import aws_sdk_application_signals.types.goal

        out["goal"] = aws_sdk_application_signals.types.goal.deserialize_json(
            data["Goal"]
        )
    return out
