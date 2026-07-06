"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListWorkloadSharesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.next_token
    import aws_sdk_wellarchitected.types.workload_id
    import aws_sdk_wellarchitected.types.workload_share_summaries


class ListWorkloadSharesOutput(TypedDict, closed=True):
    workload_id: NotRequired["aws_sdk_wellarchitected.types.workload_id.WorkloadId"]
    workload_share_summaries: NotRequired[
        "aws_sdk_wellarchitected.types.workload_share_summaries.WorkloadShareSummaries"
    ]
    next_token: NotRequired["aws_sdk_wellarchitected.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkloadSharesOutput) -> dict:
    out: dict = {}
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    if "workload_share_summaries" in value:
        import aws_sdk_wellarchitected.types.workload_share_summaries

        out["WorkloadShareSummaries"] = (
            aws_sdk_wellarchitected.types.workload_share_summaries.serialize_json(
                value["workload_share_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWorkloadSharesOutput:
    out: ListWorkloadSharesOutput = {}  # type: ignore[typeddict-item]
    if "WorkloadId" in data:
        out["workload_id"] = data["WorkloadId"]
    if "WorkloadShareSummaries" in data:
        import aws_sdk_wellarchitected.types.workload_share_summaries

        out["workload_share_summaries"] = (
            aws_sdk_wellarchitected.types.workload_share_summaries.deserialize_json(
                data["WorkloadShareSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
