"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetLensReviewReportInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.lens_alias
    import capo_wellarchitected.types.milestone_number
    import capo_wellarchitected.types.workload_id


class GetLensReviewReportInput(TypedDict, closed=True):
    workload_id: "capo_wellarchitected.types.workload_id.WorkloadId"
    lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias"
    milestone_number: NotRequired[
        "capo_wellarchitected.types.milestone_number.MilestoneNumber"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetLensReviewReportInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLensReviewReportInput:
    out: GetLensReviewReportInput = {}  # type: ignore[typeddict-item]
    return out
