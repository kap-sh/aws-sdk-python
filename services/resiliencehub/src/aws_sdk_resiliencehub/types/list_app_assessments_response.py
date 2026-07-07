"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListAppAssessmentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.app_assessment_summary_list
    import aws_sdk_resiliencehub.types.next_token


class ListAppAssessmentsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_resiliencehub.types.next_token.NextToken"]
    """<p>Token for the next set of results, or null if there are no more results.</p>"""
    assessment_summaries: "aws_sdk_resiliencehub.types.app_assessment_summary_list.AppAssessmentSummaryList"
    """<p>The summaries for the specified assessments, returned as an object. This object includes application versions, associated Amazon Resource Numbers (ARNs), cost, messages, resiliency scores, and more.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppAssessmentsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_resiliencehub.types.app_assessment_summary_list

    out["assessmentSummaries"] = (
        aws_sdk_resiliencehub.types.app_assessment_summary_list.serialize_json(
            value["assessment_summaries"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListAppAssessmentsResponse:
    out: ListAppAssessmentsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "assessmentSummaries" in data:
        import aws_sdk_resiliencehub.types.app_assessment_summary_list

        out["assessment_summaries"] = (
            aws_sdk_resiliencehub.types.app_assessment_summary_list.deserialize_json(
                data["assessmentSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListAppAssessmentsResponse.assessment_summaries required"
        )
    return out
