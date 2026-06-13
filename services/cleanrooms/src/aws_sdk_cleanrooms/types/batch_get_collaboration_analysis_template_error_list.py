"""Generated from Smithy shape ``com.amazonaws.cleanrooms#BatchGetCollaborationAnalysisTemplateErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.batch_get_collaboration_analysis_template_error

BatchGetCollaborationAnalysisTemplateErrorList: TypeAlias = list[
    "aws_sdk_cleanrooms.types.batch_get_collaboration_analysis_template_error.BatchGetCollaborationAnalysisTemplateError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCollaborationAnalysisTemplateErrorList) -> list:
    import aws_sdk_cleanrooms.types.batch_get_collaboration_analysis_template_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanrooms.types.batch_get_collaboration_analysis_template_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchGetCollaborationAnalysisTemplateErrorList:
    import aws_sdk_cleanrooms.types.batch_get_collaboration_analysis_template_error

    out: BatchGetCollaborationAnalysisTemplateErrorList = []
    for item in data:
        out.append(
            aws_sdk_cleanrooms.types.batch_get_collaboration_analysis_template_error.deserialize_json(
                item
            )
        )
    return out
