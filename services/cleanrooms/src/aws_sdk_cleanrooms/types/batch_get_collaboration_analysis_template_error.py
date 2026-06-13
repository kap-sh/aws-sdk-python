"""Generated from Smithy shape ``com.amazonaws.cleanrooms#BatchGetCollaborationAnalysisTemplateError``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.analysis_template_arn


class BatchGetCollaborationAnalysisTemplateError(TypedDict):
    arn: "aws_sdk_cleanrooms.types.analysis_template_arn.AnalysisTemplateArn"
    """<p>The Amazon Resource Name (ARN) of the analysis template.</p>"""
    code: "str"
    """<p>An error code for the error.</p>"""
    message: "str"
    """<p>A description of why the call failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCollaborationAnalysisTemplateError) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["code"] = value["code"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchGetCollaborationAnalysisTemplateError:
    out: BatchGetCollaborationAnalysisTemplateError = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError(
            "BatchGetCollaborationAnalysisTemplateError.arn required"
        )
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError(
            "BatchGetCollaborationAnalysisTemplateError.code required"
        )
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError(
            "BatchGetCollaborationAnalysisTemplateError.message required"
        )
    return out
