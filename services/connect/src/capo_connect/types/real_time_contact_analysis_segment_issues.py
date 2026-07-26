"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisSegmentIssues``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.real_time_contact_analysis_issues_detected


class RealTimeContactAnalysisSegmentIssues(TypedDict, closed=True):
    issues_detected: "capo_connect.types.real_time_contact_analysis_issues_detected.RealTimeContactAnalysisIssuesDetected"
    """<p>List of the issues detected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisSegmentIssues) -> dict:
    out: dict = {}
    import capo_connect.types.real_time_contact_analysis_issues_detected

    out["IssuesDetected"] = (
        capo_connect.types.real_time_contact_analysis_issues_detected.serialize_json(
            value["issues_detected"]
        )
    )
    return out


def deserialize_json(data: dict) -> RealTimeContactAnalysisSegmentIssues:
    out: RealTimeContactAnalysisSegmentIssues = {}  # type: ignore[typeddict-item]
    if "IssuesDetected" in data:
        import capo_connect.types.real_time_contact_analysis_issues_detected

        out["issues_detected"] = (
            capo_connect.types.real_time_contact_analysis_issues_detected.deserialize_json(
                data["IssuesDetected"]
            )
        )
    else:
        raise DeserializationError(
            "RealTimeContactAnalysisSegmentIssues.issues_detected required"
        )
    return out
