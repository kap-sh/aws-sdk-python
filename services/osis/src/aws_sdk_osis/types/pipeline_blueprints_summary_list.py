"""Generated from Smithy shape ``com.amazonaws.osis#PipelineBlueprintsSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_osis.types.pipeline_blueprint_summary

PipelineBlueprintsSummaryList: TypeAlias = list[
    "aws_sdk_osis.types.pipeline_blueprint_summary.PipelineBlueprintSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PipelineBlueprintsSummaryList) -> list:
    import aws_sdk_osis.types.pipeline_blueprint_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_osis.types.pipeline_blueprint_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> PipelineBlueprintsSummaryList:
    import aws_sdk_osis.types.pipeline_blueprint_summary

    out: PipelineBlueprintsSummaryList = []
    for item in data:
        out.append(aws_sdk_osis.types.pipeline_blueprint_summary.deserialize_json(item))
    return out
