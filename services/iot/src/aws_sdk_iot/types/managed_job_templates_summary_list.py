"""Generated from Smithy shape ``com.amazonaws.iot#ManagedJobTemplatesSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.managed_job_template_summary

ManagedJobTemplatesSummaryList: TypeAlias = list[
    "aws_sdk_iot.types.managed_job_template_summary.ManagedJobTemplateSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ManagedJobTemplatesSummaryList) -> list:
    import aws_sdk_iot.types.managed_job_template_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.managed_job_template_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ManagedJobTemplatesSummaryList:
    import aws_sdk_iot.types.managed_job_template_summary

    out: ManagedJobTemplatesSummaryList = []
    for item in data:
        out.append(
            aws_sdk_iot.types.managed_job_template_summary.deserialize_json(item)
        )
    return out
