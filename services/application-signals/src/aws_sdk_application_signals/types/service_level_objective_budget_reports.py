"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceLevelObjectiveBudgetReports``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.service_level_objective_budget_report

ServiceLevelObjectiveBudgetReports: TypeAlias = list[
    "aws_sdk_application_signals.types.service_level_objective_budget_report.ServiceLevelObjectiveBudgetReport"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceLevelObjectiveBudgetReports) -> list:
    import aws_sdk_application_signals.types.service_level_objective_budget_report

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_signals.types.service_level_objective_budget_report.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ServiceLevelObjectiveBudgetReports:
    import aws_sdk_application_signals.types.service_level_objective_budget_report

    out: ServiceLevelObjectiveBudgetReports = []
    for item in data:
        out.append(
            aws_sdk_application_signals.types.service_level_objective_budget_report.deserialize_json(
                item
            )
        )
    return out
