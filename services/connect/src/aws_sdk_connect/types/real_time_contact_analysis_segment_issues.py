"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisSegmentIssues``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.real_time_contact_analysis_issues_detected


class RealTimeContactAnalysisSegmentIssues(TypedDict):
    issues_detected: "aws_sdk_connect.types.real_time_contact_analysis_issues_detected.RealTimeContactAnalysisIssuesDetected"
    """<p>List of the issues detected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisSegmentIssues) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.real_time_contact_analysis_issues_detected

    out["IssuesDetected"] = (
        aws_sdk_connect.types.real_time_contact_analysis_issues_detected.serialize_json(
            value["issues_detected"]
        )
    )
    return out


def deserialize_json(data: dict) -> RealTimeContactAnalysisSegmentIssues:
    out: RealTimeContactAnalysisSegmentIssues = {}  # type: ignore[typeddict-item]
    if "IssuesDetected" in data:
        import aws_sdk_connect.types.real_time_contact_analysis_issues_detected

        out["issues_detected"] = (
            aws_sdk_connect.types.real_time_contact_analysis_issues_detected.deserialize_json(
                data["IssuesDetected"]
            )
        )
    else:
        raise DeserializationError(
            "RealTimeContactAnalysisSegmentIssues.issues_detected required"
        )
    return out
