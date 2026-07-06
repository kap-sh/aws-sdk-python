"""Generated from Smithy shape ``com.amazonaws.cleanrooms#BatchGetCollaborationAnalysisTemplateOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.batch_get_collaboration_analysis_template_error_list
    import aws_sdk_cleanrooms.types.collaboration_analysis_template_list


class BatchGetCollaborationAnalysisTemplateOutput(TypedDict, closed=True):
    collaboration_analysis_templates: "aws_sdk_cleanrooms.types.collaboration_analysis_template_list.CollaborationAnalysisTemplateList"
    """<p>The retrieved list of analysis templates within a collaboration.</p>"""
    errors: "aws_sdk_cleanrooms.types.batch_get_collaboration_analysis_template_error_list.BatchGetCollaborationAnalysisTemplateErrorList"
    """<p>Error reasons for collaboration analysis templates that could not be retrieved. One error is returned for every collaboration analysis template that could not be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCollaborationAnalysisTemplateOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.collaboration_analysis_template_list

    out["collaborationAnalysisTemplates"] = (
        aws_sdk_cleanrooms.types.collaboration_analysis_template_list.serialize_json(
            value["collaboration_analysis_templates"]
        )
    )
    import aws_sdk_cleanrooms.types.batch_get_collaboration_analysis_template_error_list

    out["errors"] = (
        aws_sdk_cleanrooms.types.batch_get_collaboration_analysis_template_error_list.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetCollaborationAnalysisTemplateOutput:
    out: BatchGetCollaborationAnalysisTemplateOutput = {}  # type: ignore[typeddict-item]
    if "collaborationAnalysisTemplates" in data:
        import aws_sdk_cleanrooms.types.collaboration_analysis_template_list

        out["collaboration_analysis_templates"] = (
            aws_sdk_cleanrooms.types.collaboration_analysis_template_list.deserialize_json(
                data["collaborationAnalysisTemplates"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetCollaborationAnalysisTemplateOutput.collaboration_analysis_templates required"
        )
    if "errors" in data:
        import aws_sdk_cleanrooms.types.batch_get_collaboration_analysis_template_error_list

        out["errors"] = (
            aws_sdk_cleanrooms.types.batch_get_collaboration_analysis_template_error_list.deserialize_json(
                data["errors"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetCollaborationAnalysisTemplateOutput.errors required"
        )
    return out
