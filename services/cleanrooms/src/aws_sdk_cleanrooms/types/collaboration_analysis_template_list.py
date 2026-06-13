"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CollaborationAnalysisTemplateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.collaboration_analysis_template

CollaborationAnalysisTemplateList: TypeAlias = list[
    "aws_sdk_cleanrooms.types.collaboration_analysis_template.CollaborationAnalysisTemplate"
]


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationAnalysisTemplateList) -> list:
    import aws_sdk_cleanrooms.types.collaboration_analysis_template

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanrooms.types.collaboration_analysis_template.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CollaborationAnalysisTemplateList:
    import aws_sdk_cleanrooms.types.collaboration_analysis_template

    out: CollaborationAnalysisTemplateList = []
    for item in data:
        out.append(
            aws_sdk_cleanrooms.types.collaboration_analysis_template.deserialize_json(
                item
            )
        )
    return out
