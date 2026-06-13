"""Generated from Smithy shape ``com.amazonaws.securityagent#ListCodeReviewJobsForCodeReviewOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.code_review_job_summary_list
    import aws_sdk_securityagent.types.next_token


class ListCodeReviewJobsForCodeReviewOutput(TypedDict):
    code_review_job_summaries: NotRequired[
        "aws_sdk_securityagent.types.code_review_job_summary_list.CodeReviewJobSummaryList"
    ]
    """<p>The list of code review job summaries.</p>"""
    next_token: NotRequired["aws_sdk_securityagent.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCodeReviewJobsForCodeReviewOutput) -> dict:
    out: dict = {}
    if "code_review_job_summaries" in value:
        import aws_sdk_securityagent.types.code_review_job_summary_list

        out["codeReviewJobSummaries"] = (
            aws_sdk_securityagent.types.code_review_job_summary_list.serialize_json(
                value["code_review_job_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCodeReviewJobsForCodeReviewOutput:
    out: ListCodeReviewJobsForCodeReviewOutput = {}  # type: ignore[typeddict-item]
    if "codeReviewJobSummaries" in data:
        import aws_sdk_securityagent.types.code_review_job_summary_list

        out["code_review_job_summaries"] = (
            aws_sdk_securityagent.types.code_review_job_summary_list.deserialize_json(
                data["codeReviewJobSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
