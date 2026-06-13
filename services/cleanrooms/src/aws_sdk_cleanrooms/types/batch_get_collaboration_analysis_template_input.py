"""Generated from Smithy shape ``com.amazonaws.cleanrooms#BatchGetCollaborationAnalysisTemplateInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.analysis_template_arn_list
    import aws_sdk_cleanrooms.types.collaboration_identifier


class BatchGetCollaborationAnalysisTemplateInput(TypedDict):
    collaboration_identifier: (
        "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>A unique identifier for the collaboration that the analysis templates belong to. Currently accepts collaboration ID.</p>"""
    analysis_template_arns: (
        "aws_sdk_cleanrooms.types.analysis_template_arn_list.AnalysisTemplateArnList"
    )
    """<p>The Amazon Resource Name (ARN) associated with the analysis template within a collaboration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCollaborationAnalysisTemplateInput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.analysis_template_arn_list

    out["analysisTemplateArns"] = (
        aws_sdk_cleanrooms.types.analysis_template_arn_list.serialize_json(
            value["analysis_template_arns"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetCollaborationAnalysisTemplateInput:
    out: BatchGetCollaborationAnalysisTemplateInput = {}  # type: ignore[typeddict-item]
    if "analysisTemplateArns" in data:
        import aws_sdk_cleanrooms.types.analysis_template_arn_list

        out["analysis_template_arns"] = (
            aws_sdk_cleanrooms.types.analysis_template_arn_list.deserialize_json(
                data["analysisTemplateArns"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetCollaborationAnalysisTemplateInput.analysis_template_arns required"
        )
    return out
