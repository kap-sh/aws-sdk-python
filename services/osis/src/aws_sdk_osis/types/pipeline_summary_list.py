"""Generated from Smithy shape ``com.amazonaws.osis#PipelineSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_osis.types.pipeline_summary

PipelineSummaryList: TypeAlias = list[
    "aws_sdk_osis.types.pipeline_summary.PipelineSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PipelineSummaryList) -> list:
    import aws_sdk_osis.types.pipeline_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_osis.types.pipeline_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> PipelineSummaryList:
    import aws_sdk_osis.types.pipeline_summary

    out: PipelineSummaryList = []
    for item in data:
        out.append(aws_sdk_osis.types.pipeline_summary.deserialize_json(item))
    return out
