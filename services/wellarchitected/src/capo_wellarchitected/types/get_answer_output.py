"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetAnswerOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.answer
    import capo_wellarchitected.types.lens_alias
    import capo_wellarchitected.types.lens_arn
    import capo_wellarchitected.types.milestone_number
    import capo_wellarchitected.types.workload_id


class GetAnswerOutput(TypedDict, closed=True):
    workload_id: NotRequired["capo_wellarchitected.types.workload_id.WorkloadId"]
    milestone_number: NotRequired[
        "capo_wellarchitected.types.milestone_number.MilestoneNumber"
    ]
    lens_alias: NotRequired["capo_wellarchitected.types.lens_alias.LensAlias"]
    lens_arn: NotRequired["capo_wellarchitected.types.lens_arn.LensArn"]
    """<p>The ARN for the lens.</p>"""
    answer: NotRequired["capo_wellarchitected.types.answer.Answer"]


# --- restJson1 ser/de ---
def serialize_json(value: GetAnswerOutput) -> dict:
    out: dict = {}
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    if "milestone_number" in value:
        out["MilestoneNumber"] = value["milestone_number"]
    if "lens_alias" in value:
        out["LensAlias"] = value["lens_alias"]
    if "lens_arn" in value:
        out["LensArn"] = value["lens_arn"]
    if "answer" in value:
        import capo_wellarchitected.types.answer

        out["Answer"] = capo_wellarchitected.types.answer.serialize_json(
            value["answer"]
        )
    return out


def deserialize_json(data: dict) -> GetAnswerOutput:
    out: GetAnswerOutput = {}  # type: ignore[typeddict-item]
    if "WorkloadId" in data:
        out["workload_id"] = data["WorkloadId"]
    if "MilestoneNumber" in data:
        out["milestone_number"] = data["MilestoneNumber"]
    if "LensAlias" in data:
        out["lens_alias"] = data["LensAlias"]
    if "LensArn" in data:
        out["lens_arn"] = data["LensArn"]
    if "Answer" in data:
        import capo_wellarchitected.types.answer

        out["answer"] = capo_wellarchitected.types.answer.deserialize_json(
            data["Answer"]
        )
    return out
