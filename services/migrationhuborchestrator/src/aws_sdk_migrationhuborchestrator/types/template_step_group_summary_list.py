"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#TemplateStepGroupSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.template_step_group_summary

TemplateStepGroupSummaryList: TypeAlias = list[
    "aws_sdk_migrationhuborchestrator.types.template_step_group_summary.TemplateStepGroupSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TemplateStepGroupSummaryList) -> list:
    import aws_sdk_migrationhuborchestrator.types.template_step_group_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_migrationhuborchestrator.types.template_step_group_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TemplateStepGroupSummaryList:
    import aws_sdk_migrationhuborchestrator.types.template_step_group_summary

    out: TemplateStepGroupSummaryList = []
    for item in data:
        out.append(
            aws_sdk_migrationhuborchestrator.types.template_step_group_summary.deserialize_json(
                item
            )
        )
    return out
