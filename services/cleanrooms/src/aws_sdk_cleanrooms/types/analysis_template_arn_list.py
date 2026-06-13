"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisTemplateArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.analysis_template_arn

AnalysisTemplateArnList: TypeAlias = list[
    "aws_sdk_cleanrooms.types.analysis_template_arn.AnalysisTemplateArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisTemplateArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> AnalysisTemplateArnList:
    return list(data)
