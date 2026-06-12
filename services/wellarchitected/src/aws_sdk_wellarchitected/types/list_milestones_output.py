"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListMilestonesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.milestone_summaries
    import aws_sdk_wellarchitected.types.next_token
    import aws_sdk_wellarchitected.types.workload_id


class ListMilestonesOutput(TypedDict):
    workload_id: NotRequired["aws_sdk_wellarchitected.types.workload_id.WorkloadId"]
    milestone_summaries: NotRequired[
        "aws_sdk_wellarchitected.types.milestone_summaries.MilestoneSummaries"
    ]
    next_token: NotRequired["aws_sdk_wellarchitected.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListMilestonesOutput) -> dict:
    out: dict = {}
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    if "milestone_summaries" in value:
        import aws_sdk_wellarchitected.types.milestone_summaries

        out["MilestoneSummaries"] = (
            aws_sdk_wellarchitected.types.milestone_summaries.serialize_json(
                value["milestone_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMilestonesOutput:
    out: ListMilestonesOutput = {}  # type: ignore[typeddict-item]
    if "WorkloadId" in data:
        out["workload_id"] = data["WorkloadId"]
    if "MilestoneSummaries" in data:
        import aws_sdk_wellarchitected.types.milestone_summaries

        out["milestone_summaries"] = (
            aws_sdk_wellarchitected.types.milestone_summaries.deserialize_json(
                data["MilestoneSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
