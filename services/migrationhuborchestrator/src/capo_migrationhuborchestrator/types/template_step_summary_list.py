"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#TemplateStepSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.template_step_summary

TemplateStepSummaryList: TypeAlias = list[
    "capo_migrationhuborchestrator.types.template_step_summary.TemplateStepSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TemplateStepSummaryList) -> list:
    import capo_migrationhuborchestrator.types.template_step_summary

    out: list = []
    for item in value:
        out.append(
            capo_migrationhuborchestrator.types.template_step_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TemplateStepSummaryList:
    import capo_migrationhuborchestrator.types.template_step_summary

    out: TemplateStepSummaryList = []
    for item in data:
        out.append(
            capo_migrationhuborchestrator.types.template_step_summary.deserialize_json(
                item
            )
        )
    return out
