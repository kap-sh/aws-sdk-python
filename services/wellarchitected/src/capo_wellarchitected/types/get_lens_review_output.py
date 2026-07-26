"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetLensReviewOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.lens_review
    import capo_wellarchitected.types.milestone_number
    import capo_wellarchitected.types.workload_id


class GetLensReviewOutput(TypedDict, closed=True):
    workload_id: NotRequired["capo_wellarchitected.types.workload_id.WorkloadId"]
    milestone_number: NotRequired[
        "capo_wellarchitected.types.milestone_number.MilestoneNumber"
    ]
    lens_review: NotRequired["capo_wellarchitected.types.lens_review.LensReview"]


# --- restJson1 ser/de ---
def serialize_json(value: GetLensReviewOutput) -> dict:
    out: dict = {}
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    if "milestone_number" in value:
        out["MilestoneNumber"] = value["milestone_number"]
    if "lens_review" in value:
        import capo_wellarchitected.types.lens_review

        out["LensReview"] = capo_wellarchitected.types.lens_review.serialize_json(
            value["lens_review"]
        )
    return out


def deserialize_json(data: dict) -> GetLensReviewOutput:
    out: GetLensReviewOutput = {}  # type: ignore[typeddict-item]
    if "WorkloadId" in data:
        out["workload_id"] = data["WorkloadId"]
    if "MilestoneNumber" in data:
        out["milestone_number"] = data["MilestoneNumber"]
    if "LensReview" in data:
        import capo_wellarchitected.types.lens_review

        out["lens_review"] = capo_wellarchitected.types.lens_review.deserialize_json(
            data["LensReview"]
        )
    return out
