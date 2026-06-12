"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetAnswerInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.lens_alias
    import aws_sdk_wellarchitected.types.milestone_number
    import aws_sdk_wellarchitected.types.question_id
    import aws_sdk_wellarchitected.types.workload_id


class GetAnswerInput(TypedDict):
    workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId"
    lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias"
    question_id: "aws_sdk_wellarchitected.types.question_id.QuestionId"
    milestone_number: NotRequired[
        "aws_sdk_wellarchitected.types.milestone_number.MilestoneNumber"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetAnswerInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAnswerInput:
    out: GetAnswerInput = {}  # type: ignore[typeddict-item]
    return out
