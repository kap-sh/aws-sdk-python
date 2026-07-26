"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListCheckDetailsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.choice_id
    import capo_wellarchitected.types.lens_arn
    import capo_wellarchitected.types.max_results
    import capo_wellarchitected.types.next_token
    import capo_wellarchitected.types.pillar_id
    import capo_wellarchitected.types.question_id
    import capo_wellarchitected.types.workload_id


class ListCheckDetailsInput(TypedDict, closed=True):
    workload_id: "capo_wellarchitected.types.workload_id.WorkloadId"
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]
    max_results: NotRequired["capo_wellarchitected.types.max_results.MaxResults"]
    lens_arn: NotRequired["capo_wellarchitected.types.lens_arn.LensArn"]
    """<p>Well-Architected Lens ARN.</p>"""
    pillar_id: NotRequired["capo_wellarchitected.types.pillar_id.PillarId"]
    question_id: NotRequired["capo_wellarchitected.types.question_id.QuestionId"]
    choice_id: NotRequired["capo_wellarchitected.types.choice_id.ChoiceId"]


# --- restJson1 ser/de ---
def serialize_json(value: ListCheckDetailsInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "lens_arn" in value:
        out["LensArn"] = value["lens_arn"]
    if "pillar_id" in value:
        out["PillarId"] = value["pillar_id"]
    if "question_id" in value:
        out["QuestionId"] = value["question_id"]
    if "choice_id" in value:
        out["ChoiceId"] = value["choice_id"]
    return out


def deserialize_json(data: dict) -> ListCheckDetailsInput:
    out: ListCheckDetailsInput = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "LensArn" in data:
        out["lens_arn"] = data["LensArn"]
    if "PillarId" in data:
        out["pillar_id"] = data["PillarId"]
    if "QuestionId" in data:
        out["question_id"] = data["QuestionId"]
    if "ChoiceId" in data:
        out["choice_id"] = data["ChoiceId"]
    return out
