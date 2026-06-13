"""Generated from Smithy shape ``com.amazonaws.quicksight#TemplateVersionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.template_version_summary

TemplateVersionSummaryList: TypeAlias = list[
    "aws_sdk_quicksight.types.template_version_summary.TemplateVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TemplateVersionSummaryList) -> list:
    import aws_sdk_quicksight.types.template_version_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.template_version_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TemplateVersionSummaryList:
    import aws_sdk_quicksight.types.template_version_summary

    out: TemplateVersionSummaryList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.template_version_summary.deserialize_json(item)
        )
    return out
