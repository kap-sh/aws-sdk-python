"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListLensReviewsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.lens_review_summaries
    import aws_sdk_wellarchitected.types.milestone_number
    import aws_sdk_wellarchitected.types.next_token
    import aws_sdk_wellarchitected.types.workload_id


class ListLensReviewsOutput(TypedDict, closed=True):
    workload_id: NotRequired["aws_sdk_wellarchitected.types.workload_id.WorkloadId"]
    milestone_number: NotRequired[
        "aws_sdk_wellarchitected.types.milestone_number.MilestoneNumber"
    ]
    lens_review_summaries: NotRequired[
        "aws_sdk_wellarchitected.types.lens_review_summaries.LensReviewSummaries"
    ]
    next_token: NotRequired["aws_sdk_wellarchitected.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListLensReviewsOutput) -> dict:
    out: dict = {}
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    if "milestone_number" in value:
        out["MilestoneNumber"] = value["milestone_number"]
    if "lens_review_summaries" in value:
        import aws_sdk_wellarchitected.types.lens_review_summaries

        out["LensReviewSummaries"] = (
            aws_sdk_wellarchitected.types.lens_review_summaries.serialize_json(
                value["lens_review_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLensReviewsOutput:
    out: ListLensReviewsOutput = {}  # type: ignore[typeddict-item]
    if "WorkloadId" in data:
        out["workload_id"] = data["WorkloadId"]
    if "MilestoneNumber" in data:
        out["milestone_number"] = data["MilestoneNumber"]
    if "LensReviewSummaries" in data:
        import aws_sdk_wellarchitected.types.lens_review_summaries

        out["lens_review_summaries"] = (
            aws_sdk_wellarchitected.types.lens_review_summaries.deserialize_json(
                data["LensReviewSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
