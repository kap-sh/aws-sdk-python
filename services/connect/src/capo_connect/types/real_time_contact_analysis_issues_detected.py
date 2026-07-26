"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisIssuesDetected``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.real_time_contact_analysis_issue_detected

RealTimeContactAnalysisIssuesDetected: TypeAlias = list[
    "capo_connect.types.real_time_contact_analysis_issue_detected.RealTimeContactAnalysisIssueDetected"
]


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisIssuesDetected) -> list:
    import capo_connect.types.real_time_contact_analysis_issue_detected

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.real_time_contact_analysis_issue_detected.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RealTimeContactAnalysisIssuesDetected:
    import capo_connect.types.real_time_contact_analysis_issue_detected

    out: RealTimeContactAnalysisIssuesDetected = []
    for item in data:
        out.append(
            capo_connect.types.real_time_contact_analysis_issue_detected.deserialize_json(
                item
            )
        )
    return out
