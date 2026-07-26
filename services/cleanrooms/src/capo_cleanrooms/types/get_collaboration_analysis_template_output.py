"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetCollaborationAnalysisTemplateOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.collaboration_analysis_template


class GetCollaborationAnalysisTemplateOutput(TypedDict, closed=True):
    collaboration_analysis_template: "capo_cleanrooms.types.collaboration_analysis_template.CollaborationAnalysisTemplate"
    """<p>The analysis template within a collaboration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCollaborationAnalysisTemplateOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.collaboration_analysis_template

    out["collaborationAnalysisTemplate"] = (
        capo_cleanrooms.types.collaboration_analysis_template.serialize_json(
            value["collaboration_analysis_template"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetCollaborationAnalysisTemplateOutput:
    out: GetCollaborationAnalysisTemplateOutput = {}  # type: ignore[typeddict-item]
    if "collaborationAnalysisTemplate" in data:
        import capo_cleanrooms.types.collaboration_analysis_template

        out["collaboration_analysis_template"] = (
            capo_cleanrooms.types.collaboration_analysis_template.deserialize_json(
                data["collaborationAnalysisTemplate"]
            )
        )
    else:
        raise DeserializationError(
            "GetCollaborationAnalysisTemplateOutput.collaboration_analysis_template required"
        )
    return out
