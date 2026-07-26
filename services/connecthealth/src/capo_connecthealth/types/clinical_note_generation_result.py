"""Generated from Smithy shape ``com.amazonaws.connecthealth#ClinicalNoteGenerationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.artifact_details


class ClinicalNoteGenerationResult(TypedDict, closed=True):
    note_result: NotRequired[
        "capo_connecthealth.types.artifact_details.ArtifactDetails"
    ]
    """<p>Details about the generated clinical note</p>"""
    transcript_result: NotRequired[
        "capo_connecthealth.types.artifact_details.ArtifactDetails"
    ]
    """<p>Details about the generated transcript</p>"""
    after_visit_summary_result: NotRequired[
        "capo_connecthealth.types.artifact_details.ArtifactDetails"
    ]
    """<p>Details about the generated after visit summary</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClinicalNoteGenerationResult) -> dict:
    out: dict = {}
    if "note_result" in value:
        import capo_connecthealth.types.artifact_details

        out["noteResult"] = capo_connecthealth.types.artifact_details.serialize_json(
            value["note_result"]
        )
    if "transcript_result" in value:
        import capo_connecthealth.types.artifact_details

        out["transcriptResult"] = (
            capo_connecthealth.types.artifact_details.serialize_json(
                value["transcript_result"]
            )
        )
    if "after_visit_summary_result" in value:
        import capo_connecthealth.types.artifact_details

        out["afterVisitSummaryResult"] = (
            capo_connecthealth.types.artifact_details.serialize_json(
                value["after_visit_summary_result"]
            )
        )
    return out


def deserialize_json(data: dict) -> ClinicalNoteGenerationResult:
    out: ClinicalNoteGenerationResult = {}  # type: ignore[typeddict-item]
    if "noteResult" in data:
        import capo_connecthealth.types.artifact_details

        out["note_result"] = capo_connecthealth.types.artifact_details.deserialize_json(
            data["noteResult"]
        )
    if "transcriptResult" in data:
        import capo_connecthealth.types.artifact_details

        out["transcript_result"] = (
            capo_connecthealth.types.artifact_details.deserialize_json(
                data["transcriptResult"]
            )
        )
    if "afterVisitSummaryResult" in data:
        import capo_connecthealth.types.artifact_details

        out["after_visit_summary_result"] = (
            capo_connecthealth.types.artifact_details.deserialize_json(
                data["afterVisitSummaryResult"]
            )
        )
    return out
