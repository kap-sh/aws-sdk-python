"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListFailureModeAssessmentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.assessment_summary_list
    import aws_sdk_resiliencehubv2.types.next_token


class ListFailureModeAssessmentsResponse(TypedDict, closed=True):
    assessment_summaries: (
        "aws_sdk_resiliencehubv2.types.assessment_summary_list.AssessmentSummaryList"
    )
    """<p>The list of assessment summaries.</p>"""
    next_token: NotRequired["aws_sdk_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListFailureModeAssessmentsResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehubv2.types.assessment_summary_list

    out["assessmentSummaries"] = (
        aws_sdk_resiliencehubv2.types.assessment_summary_list.serialize_json(
            value["assessment_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFailureModeAssessmentsResponse:
    out: ListFailureModeAssessmentsResponse = {}  # type: ignore[typeddict-item]
    if "assessmentSummaries" in data:
        import aws_sdk_resiliencehubv2.types.assessment_summary_list

        out["assessment_summaries"] = (
            aws_sdk_resiliencehubv2.types.assessment_summary_list.deserialize_json(
                data["assessmentSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListFailureModeAssessmentsResponse.assessment_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
