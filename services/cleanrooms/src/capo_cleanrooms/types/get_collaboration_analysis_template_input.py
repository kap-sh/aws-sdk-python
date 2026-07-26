"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetCollaborationAnalysisTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_template_arn
    import capo_cleanrooms.types.collaboration_identifier


class GetCollaborationAnalysisTemplateInput(TypedDict, closed=True):
    collaboration_identifier: (
        "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>A unique identifier for the collaboration that the analysis templates belong to. Currently accepts collaboration ID.</p>"""
    analysis_template_arn: (
        "capo_cleanrooms.types.analysis_template_arn.AnalysisTemplateArn"
    )
    """<p>The Amazon Resource Name (ARN) associated with the analysis template within a collaboration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCollaborationAnalysisTemplateInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCollaborationAnalysisTemplateInput:
    out: GetCollaborationAnalysisTemplateInput = {}  # type: ignore[typeddict-item]
    return out
