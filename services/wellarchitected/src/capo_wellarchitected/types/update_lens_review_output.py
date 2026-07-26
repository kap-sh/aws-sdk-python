"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpdateLensReviewOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.lens_review
    import capo_wellarchitected.types.workload_id


class UpdateLensReviewOutput(TypedDict, closed=True):
    workload_id: NotRequired["capo_wellarchitected.types.workload_id.WorkloadId"]
    lens_review: NotRequired["capo_wellarchitected.types.lens_review.LensReview"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLensReviewOutput) -> dict:
    out: dict = {}
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    if "lens_review" in value:
        import capo_wellarchitected.types.lens_review

        out["LensReview"] = capo_wellarchitected.types.lens_review.serialize_json(
            value["lens_review"]
        )
    return out


def deserialize_json(data: dict) -> UpdateLensReviewOutput:
    out: UpdateLensReviewOutput = {}  # type: ignore[typeddict-item]
    if "WorkloadId" in data:
        out["workload_id"] = data["WorkloadId"]
    if "LensReview" in data:
        import capo_wellarchitected.types.lens_review

        out["lens_review"] = capo_wellarchitected.types.lens_review.deserialize_json(
            data["LensReview"]
        )
    return out
