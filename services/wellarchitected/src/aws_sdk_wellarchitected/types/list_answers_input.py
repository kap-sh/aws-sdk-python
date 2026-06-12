"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListAnswersInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.lens_alias
    import aws_sdk_wellarchitected.types.list_answers_max_results
    import aws_sdk_wellarchitected.types.milestone_number
    import aws_sdk_wellarchitected.types.next_token
    import aws_sdk_wellarchitected.types.pillar_id
    import aws_sdk_wellarchitected.types.question_priority
    import aws_sdk_wellarchitected.types.workload_id


class ListAnswersInput(TypedDict):
    workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId"
    lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias"
    pillar_id: NotRequired["aws_sdk_wellarchitected.types.pillar_id.PillarId"]
    milestone_number: NotRequired[
        "aws_sdk_wellarchitected.types.milestone_number.MilestoneNumber"
    ]
    next_token: NotRequired["aws_sdk_wellarchitected.types.next_token.NextToken"]
    max_results: NotRequired[
        "aws_sdk_wellarchitected.types.list_answers_max_results.ListAnswersMaxResults"
    ]
    """<p>The maximum number of results to return for this request.</p>"""
    question_priority: NotRequired[
        "aws_sdk_wellarchitected.types.question_priority.QuestionPriority"
    ]
    """<p>The priority of the question.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAnswersInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAnswersInput:
    out: ListAnswersInput = {}  # type: ignore[typeddict-item]
    return out
