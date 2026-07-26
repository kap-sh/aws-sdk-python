"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchGetCodeReviewJobsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.code_review_job_id_list
    import capo_securityagent.types.code_review_job_list


class BatchGetCodeReviewJobsOutput(TypedDict, closed=True):
    code_review_jobs: NotRequired[
        "capo_securityagent.types.code_review_job_list.CodeReviewJobList"
    ]
    """<p>The list of code review jobs that were found.</p>"""
    not_found: NotRequired[
        "capo_securityagent.types.code_review_job_id_list.CodeReviewJobIdList"
    ]
    """<p>The list of code review job identifiers that were not found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCodeReviewJobsOutput) -> dict:
    out: dict = {}
    if "code_review_jobs" in value:
        import capo_securityagent.types.code_review_job_list

        out["codeReviewJobs"] = (
            capo_securityagent.types.code_review_job_list.serialize_json(
                value["code_review_jobs"]
            )
        )
    if "not_found" in value:
        import capo_securityagent.types.code_review_job_id_list

        out["notFound"] = (
            capo_securityagent.types.code_review_job_id_list.serialize_json(
                value["not_found"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetCodeReviewJobsOutput:
    out: BatchGetCodeReviewJobsOutput = {}  # type: ignore[typeddict-item]
    if "codeReviewJobs" in data:
        import capo_securityagent.types.code_review_job_list

        out["code_review_jobs"] = (
            capo_securityagent.types.code_review_job_list.deserialize_json(
                data["codeReviewJobs"]
            )
        )
    if "notFound" in data:
        import capo_securityagent.types.code_review_job_id_list

        out["not_found"] = (
            capo_securityagent.types.code_review_job_id_list.deserialize_json(
                data["notFound"]
            )
        )
    return out
