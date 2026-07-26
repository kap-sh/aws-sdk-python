"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceLevelObjectiveBudgetReportErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_signals.types.service_level_objective_budget_report_error

ServiceLevelObjectiveBudgetReportErrors: TypeAlias = list[
    "capo_application_signals.types.service_level_objective_budget_report_error.ServiceLevelObjectiveBudgetReportError"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceLevelObjectiveBudgetReportErrors) -> list:
    import capo_application_signals.types.service_level_objective_budget_report_error

    out: list = []
    for item in value:
        out.append(
            capo_application_signals.types.service_level_objective_budget_report_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ServiceLevelObjectiveBudgetReportErrors:
    import capo_application_signals.types.service_level_objective_budget_report_error

    out: ServiceLevelObjectiveBudgetReportErrors = []
    for item in data:
        out.append(
            capo_application_signals.types.service_level_objective_budget_report_error.deserialize_json(
                item
            )
        )
    return out
