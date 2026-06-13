"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#TemplateStepSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.template_step_summary

TemplateStepSummaryList: TypeAlias = list[
    "aws_sdk_migrationhuborchestrator.types.template_step_summary.TemplateStepSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TemplateStepSummaryList) -> list:
    import aws_sdk_migrationhuborchestrator.types.template_step_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_migrationhuborchestrator.types.template_step_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TemplateStepSummaryList:
    import aws_sdk_migrationhuborchestrator.types.template_step_summary

    out: TemplateStepSummaryList = []
    for item in data:
        out.append(
            aws_sdk_migrationhuborchestrator.types.template_step_summary.deserialize_json(
                item
            )
        )
    return out
