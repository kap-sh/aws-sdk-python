"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceLevelObjectiveSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_signals.types.service_level_objective_summary

ServiceLevelObjectiveSummaries: TypeAlias = list[
    "capo_application_signals.types.service_level_objective_summary.ServiceLevelObjectiveSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceLevelObjectiveSummaries) -> list:
    import capo_application_signals.types.service_level_objective_summary

    out: list = []
    for item in value:
        out.append(
            capo_application_signals.types.service_level_objective_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ServiceLevelObjectiveSummaries:
    import capo_application_signals.types.service_level_objective_summary

    out: ServiceLevelObjectiveSummaries = []
    for item in data:
        out.append(
            capo_application_signals.types.service_level_objective_summary.deserialize_json(
                item
            )
        )
    return out
