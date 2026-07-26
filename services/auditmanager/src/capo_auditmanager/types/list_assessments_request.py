"""Generated from Smithy shape ``com.amazonaws.auditmanager#ListAssessmentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment_status
    import capo_auditmanager.types.max_results
    import capo_auditmanager.types.token


class ListAssessmentsRequest(TypedDict, closed=True):
    status: NotRequired["capo_auditmanager.types.assessment_status.AssessmentStatus"]
    """<p> The current status of the assessment.</p>"""
    next_token: NotRequired["capo_auditmanager.types.token.Token"]
    """<p> The pagination token that's used to fetch the next set of results. </p>"""
    max_results: NotRequired["capo_auditmanager.types.max_results.MaxResults"]
    """<p> Represents the maximum number of results on a page or for an API request call. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssessmentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAssessmentsRequest:
    out: ListAssessmentsRequest = {}  # type: ignore[typeddict-item]
    return out
