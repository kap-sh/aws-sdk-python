"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListLensReviewImprovementsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.improvement_summaries
    import capo_wellarchitected.types.lens_alias
    import capo_wellarchitected.types.lens_arn
    import capo_wellarchitected.types.milestone_number
    import capo_wellarchitected.types.next_token
    import capo_wellarchitected.types.workload_id


class ListLensReviewImprovementsOutput(TypedDict, closed=True):
    workload_id: NotRequired["capo_wellarchitected.types.workload_id.WorkloadId"]
    milestone_number: NotRequired[
        "capo_wellarchitected.types.milestone_number.MilestoneNumber"
    ]
    lens_alias: NotRequired["capo_wellarchitected.types.lens_alias.LensAlias"]
    lens_arn: NotRequired["capo_wellarchitected.types.lens_arn.LensArn"]
    """<p>The ARN for the lens.</p>"""
    improvement_summaries: NotRequired[
        "capo_wellarchitected.types.improvement_summaries.ImprovementSummaries"
    ]
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListLensReviewImprovementsOutput) -> dict:
    out: dict = {}
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    if "milestone_number" in value:
        out["MilestoneNumber"] = value["milestone_number"]
    if "lens_alias" in value:
        out["LensAlias"] = value["lens_alias"]
    if "lens_arn" in value:
        out["LensArn"] = value["lens_arn"]
    if "improvement_summaries" in value:
        import capo_wellarchitected.types.improvement_summaries

        out["ImprovementSummaries"] = (
            capo_wellarchitected.types.improvement_summaries.serialize_json(
                value["improvement_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLensReviewImprovementsOutput:
    out: ListLensReviewImprovementsOutput = {}  # type: ignore[typeddict-item]
    if "WorkloadId" in data:
        out["workload_id"] = data["WorkloadId"]
    if "MilestoneNumber" in data:
        out["milestone_number"] = data["MilestoneNumber"]
    if "LensAlias" in data:
        out["lens_alias"] = data["LensAlias"]
    if "LensArn" in data:
        out["lens_arn"] = data["LensArn"]
    if "ImprovementSummaries" in data:
        import capo_wellarchitected.types.improvement_summaries

        out["improvement_summaries"] = (
            capo_wellarchitected.types.improvement_summaries.deserialize_json(
                data["ImprovementSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
