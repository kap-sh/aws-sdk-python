"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListAnswersInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.lens_alias
    import capo_wellarchitected.types.list_answers_max_results
    import capo_wellarchitected.types.milestone_number
    import capo_wellarchitected.types.next_token
    import capo_wellarchitected.types.pillar_id
    import capo_wellarchitected.types.question_priority
    import capo_wellarchitected.types.workload_id


class ListAnswersInput(TypedDict, closed=True):
    workload_id: "capo_wellarchitected.types.workload_id.WorkloadId"
    lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias"
    pillar_id: NotRequired["capo_wellarchitected.types.pillar_id.PillarId"]
    milestone_number: NotRequired[
        "capo_wellarchitected.types.milestone_number.MilestoneNumber"
    ]
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]
    max_results: NotRequired[
        "capo_wellarchitected.types.list_answers_max_results.ListAnswersMaxResults"
    ]
    """<p>The maximum number of results to return for this request.</p>"""
    question_priority: NotRequired[
        "capo_wellarchitected.types.question_priority.QuestionPriority"
    ]
    """<p>The priority of the question.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAnswersInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAnswersInput:
    out: ListAnswersInput = {}  # type: ignore[typeddict-item]
    return out
