"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListAnswersOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.answer_summaries
    import aws_sdk_wellarchitected.types.lens_alias
    import aws_sdk_wellarchitected.types.lens_arn
    import aws_sdk_wellarchitected.types.milestone_number
    import aws_sdk_wellarchitected.types.next_token
    import aws_sdk_wellarchitected.types.workload_id


class ListAnswersOutput(TypedDict, closed=True):
    workload_id: NotRequired["aws_sdk_wellarchitected.types.workload_id.WorkloadId"]
    milestone_number: NotRequired[
        "aws_sdk_wellarchitected.types.milestone_number.MilestoneNumber"
    ]
    lens_alias: NotRequired["aws_sdk_wellarchitected.types.lens_alias.LensAlias"]
    lens_arn: NotRequired["aws_sdk_wellarchitected.types.lens_arn.LensArn"]
    """<p>The ARN for the lens.</p>"""
    answer_summaries: NotRequired[
        "aws_sdk_wellarchitected.types.answer_summaries.AnswerSummaries"
    ]
    next_token: NotRequired["aws_sdk_wellarchitected.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListAnswersOutput) -> dict:
    out: dict = {}
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    if "milestone_number" in value:
        out["MilestoneNumber"] = value["milestone_number"]
    if "lens_alias" in value:
        out["LensAlias"] = value["lens_alias"]
    if "lens_arn" in value:
        out["LensArn"] = value["lens_arn"]
    if "answer_summaries" in value:
        import aws_sdk_wellarchitected.types.answer_summaries

        out["AnswerSummaries"] = (
            aws_sdk_wellarchitected.types.answer_summaries.serialize_json(
                value["answer_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAnswersOutput:
    out: ListAnswersOutput = {}  # type: ignore[typeddict-item]
    if "WorkloadId" in data:
        out["workload_id"] = data["WorkloadId"]
    if "MilestoneNumber" in data:
        out["milestone_number"] = data["MilestoneNumber"]
    if "LensAlias" in data:
        out["lens_alias"] = data["LensAlias"]
    if "LensArn" in data:
        out["lens_arn"] = data["LensArn"]
    if "AnswerSummaries" in data:
        import aws_sdk_wellarchitected.types.answer_summaries

        out["answer_summaries"] = (
            aws_sdk_wellarchitected.types.answer_summaries.deserialize_json(
                data["AnswerSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
