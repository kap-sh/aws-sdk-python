"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceLevelObjectiveBudgetReportError``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.service_level_objective_arn
    import aws_sdk_application_signals.types.service_level_objective_budget_report_error_code
    import aws_sdk_application_signals.types.service_level_objective_budget_report_error_message
    import aws_sdk_application_signals.types.service_level_objective_name


class ServiceLevelObjectiveBudgetReportError(TypedDict):
    name: "aws_sdk_application_signals.types.service_level_objective_name.ServiceLevelObjectiveName"
    """<p>The name of the SLO that this error is related to.</p>"""
    arn: "aws_sdk_application_signals.types.service_level_objective_arn.ServiceLevelObjectiveArn"
    """<p>The ARN of the SLO that this error is related to.</p>"""
    error_code: "aws_sdk_application_signals.types.service_level_objective_budget_report_error_code.ServiceLevelObjectiveBudgetReportErrorCode"
    """<p>The error code for this error.</p>"""
    error_message: "aws_sdk_application_signals.types.service_level_objective_budget_report_error_message.ServiceLevelObjectiveBudgetReportErrorMessage"
    """<p>The message for this error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceLevelObjectiveBudgetReportError) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Arn"] = value["arn"]
    out["ErrorCode"] = value["error_code"]
    out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> ServiceLevelObjectiveBudgetReportError:
    out: ServiceLevelObjectiveBudgetReportError = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError(
            "ServiceLevelObjectiveBudgetReportError.name required"
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError(
            "ServiceLevelObjectiveBudgetReportError.arn required"
        )
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    else:
        raise DeserializationError(
            "ServiceLevelObjectiveBudgetReportError.error_code required"
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    else:
        raise DeserializationError(
            "ServiceLevelObjectiveBudgetReportError.error_message required"
        )
    return out
