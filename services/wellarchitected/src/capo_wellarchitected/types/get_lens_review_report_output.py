"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetLensReviewReportOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.lens_review_report
    import capo_wellarchitected.types.milestone_number
    import capo_wellarchitected.types.workload_id


class GetLensReviewReportOutput(TypedDict, closed=True):
    workload_id: NotRequired["capo_wellarchitected.types.workload_id.WorkloadId"]
    milestone_number: NotRequired[
        "capo_wellarchitected.types.milestone_number.MilestoneNumber"
    ]
    lens_review_report: NotRequired[
        "capo_wellarchitected.types.lens_review_report.LensReviewReport"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetLensReviewReportOutput) -> dict:
    out: dict = {}
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    if "milestone_number" in value:
        out["MilestoneNumber"] = value["milestone_number"]
    if "lens_review_report" in value:
        import capo_wellarchitected.types.lens_review_report

        out["LensReviewReport"] = (
            capo_wellarchitected.types.lens_review_report.serialize_json(
                value["lens_review_report"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetLensReviewReportOutput:
    out: GetLensReviewReportOutput = {}  # type: ignore[typeddict-item]
    if "WorkloadId" in data:
        out["workload_id"] = data["WorkloadId"]
    if "MilestoneNumber" in data:
        out["milestone_number"] = data["MilestoneNumber"]
    if "LensReviewReport" in data:
        import capo_wellarchitected.types.lens_review_report

        out["lens_review_report"] = (
            capo_wellarchitected.types.lens_review_report.deserialize_json(
                data["LensReviewReport"]
            )
        )
    return out
