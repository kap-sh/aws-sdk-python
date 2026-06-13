"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceLevelObjectiveBudgetReportErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.service_level_objective_budget_report_error

ServiceLevelObjectiveBudgetReportErrors: TypeAlias = list[
    "aws_sdk_application_signals.types.service_level_objective_budget_report_error.ServiceLevelObjectiveBudgetReportError"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceLevelObjectiveBudgetReportErrors) -> list:
    import aws_sdk_application_signals.types.service_level_objective_budget_report_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_signals.types.service_level_objective_budget_report_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ServiceLevelObjectiveBudgetReportErrors:
    import aws_sdk_application_signals.types.service_level_objective_budget_report_error

    out: ServiceLevelObjectiveBudgetReportErrors = []
    for item in data:
        out.append(
            aws_sdk_application_signals.types.service_level_objective_budget_report_error.deserialize_json(
                item
            )
        )
    return out
