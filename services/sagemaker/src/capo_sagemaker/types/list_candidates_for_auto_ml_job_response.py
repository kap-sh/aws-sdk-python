"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListCandidatesForAutoMLJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_ml_candidates
    import capo_sagemaker.types.next_token


class ListCandidatesForAutoMLJobResponse(TypedDict, closed=True):
    candidates: NotRequired["capo_sagemaker.types.auto_ml_candidates.AutoMLCandidates"]
    """<p>Summaries about the <code>AutoMLCandidates</code>.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCandidatesForAutoMLJobResponse) -> dict:
    out: dict = {}
    if "candidates" in value:
        import capo_sagemaker.types.auto_ml_candidates

        out["Candidates"] = (
            capo_sagemaker.types.auto_ml_candidates.serialize_aws_json_1_1(
                value["candidates"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCandidatesForAutoMLJobResponse:
    out: ListCandidatesForAutoMLJobResponse = {}  # type: ignore[typeddict-item]
    if "Candidates" in data:
        import capo_sagemaker.types.auto_ml_candidates

        out["candidates"] = (
            capo_sagemaker.types.auto_ml_candidates.deserialize_aws_json_1_1(
                data["Candidates"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
