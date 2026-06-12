"""Generated from Smithy shape ``com.amazonaws.connecthealth#ClinicalNoteGenerationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.artifact_details

class ClinicalNoteGenerationResult(TypedDict):
    note_result: NotRequired["aws_sdk_connecthealth.types.artifact_details.ArtifactDetails"]
    """<p>Details about the generated clinical note</p>"""
    transcript_result: NotRequired["aws_sdk_connecthealth.types.artifact_details.ArtifactDetails"]
    """<p>Details about the generated transcript</p>"""
    after_visit_summary_result: NotRequired["aws_sdk_connecthealth.types.artifact_details.ArtifactDetails"]
    """<p>Details about the generated after visit summary</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ClinicalNoteGenerationResult) -> dict:
    out: dict = {}
    if "note_result" in value:
        import aws_sdk_connecthealth.types.artifact_details
        out["noteResult"] = aws_sdk_connecthealth.types.artifact_details.serialize_json(value["note_result"])
    if "transcript_result" in value:
        import aws_sdk_connecthealth.types.artifact_details
        out["transcriptResult"] = aws_sdk_connecthealth.types.artifact_details.serialize_json(value["transcript_result"])
    if "after_visit_summary_result" in value:
        import aws_sdk_connecthealth.types.artifact_details
        out["afterVisitSummaryResult"] = aws_sdk_connecthealth.types.artifact_details.serialize_json(value["after_visit_summary_result"])
    return out


def deserialize_json(data: dict) -> ClinicalNoteGenerationResult:
    out: ClinicalNoteGenerationResult = {}  # type: ignore[typeddict-item]
    if "noteResult" in data:
        import aws_sdk_connecthealth.types.artifact_details
        out["note_result"] = aws_sdk_connecthealth.types.artifact_details.deserialize_json(data["noteResult"])
    if "transcriptResult" in data:
        import aws_sdk_connecthealth.types.artifact_details
        out["transcript_result"] = aws_sdk_connecthealth.types.artifact_details.deserialize_json(data["transcriptResult"])
    if "afterVisitSummaryResult" in data:
        import aws_sdk_connecthealth.types.artifact_details
        out["after_visit_summary_result"] = aws_sdk_connecthealth.types.artifact_details.deserialize_json(data["afterVisitSummaryResult"])
    return out