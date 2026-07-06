"""Generated from Smithy shape ``com.amazonaws.applicationsignals#BatchGetServiceLevelObjectiveBudgetReportOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_application_signals.types.service_level_objective_budget_report_errors
    import aws_sdk_application_signals.types.service_level_objective_budget_reports


class BatchGetServiceLevelObjectiveBudgetReportOutput(TypedDict, closed=True):
    timestamp: "datetime.datetime"
    """<p>The date and time that the report is for. It is expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC.</p>"""
    reports: "aws_sdk_application_signals.types.service_level_objective_budget_reports.ServiceLevelObjectiveBudgetReports"
    """<p>An array of structures, where each structure is one budget report.</p>"""
    errors: "aws_sdk_application_signals.types.service_level_objective_budget_report_errors.ServiceLevelObjectiveBudgetReportErrors"
    """<p>An array of structures, where each structure includes an error indicating that one of the requests in the array was not valid.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetServiceLevelObjectiveBudgetReportOutput) -> dict:
    out: dict = {}
    import aws_sdk_application_signals.types._prelude.timestamp

    out["Timestamp"] = (
        aws_sdk_application_signals.types._prelude.timestamp.serialize_json(
            value["timestamp"]
        )
    )
    import aws_sdk_application_signals.types.service_level_objective_budget_reports

    out["Reports"] = (
        aws_sdk_application_signals.types.service_level_objective_budget_reports.serialize_json(
            value["reports"]
        )
    )
    import aws_sdk_application_signals.types.service_level_objective_budget_report_errors

    out["Errors"] = (
        aws_sdk_application_signals.types.service_level_objective_budget_report_errors.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetServiceLevelObjectiveBudgetReportOutput:
    out: BatchGetServiceLevelObjectiveBudgetReportOutput = {}  # type: ignore[typeddict-item]
    if "Timestamp" in data:
        import aws_sdk_application_signals.types._prelude.timestamp

        out["timestamp"] = (
            aws_sdk_application_signals.types._prelude.timestamp.deserialize_json(
                data["Timestamp"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetServiceLevelObjectiveBudgetReportOutput.timestamp required"
        )
    if "Reports" in data:
        import aws_sdk_application_signals.types.service_level_objective_budget_reports

        out["reports"] = (
            aws_sdk_application_signals.types.service_level_objective_budget_reports.deserialize_json(
                data["Reports"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetServiceLevelObjectiveBudgetReportOutput.reports required"
        )
    if "Errors" in data:
        import aws_sdk_application_signals.types.service_level_objective_budget_report_errors

        out["errors"] = (
            aws_sdk_application_signals.types.service_level_objective_budget_report_errors.deserialize_json(
                data["Errors"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetServiceLevelObjectiveBudgetReportOutput.errors required"
        )
    return out
