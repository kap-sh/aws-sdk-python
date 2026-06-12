"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListWorkloadsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.next_token
    import aws_sdk_wellarchitected.types.workload_summaries


class ListWorkloadsOutput(TypedDict):
    workload_summaries: NotRequired[
        "aws_sdk_wellarchitected.types.workload_summaries.WorkloadSummaries"
    ]
    next_token: NotRequired["aws_sdk_wellarchitected.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkloadsOutput) -> dict:
    out: dict = {}
    if "workload_summaries" in value:
        import aws_sdk_wellarchitected.types.workload_summaries

        out["WorkloadSummaries"] = (
            aws_sdk_wellarchitected.types.workload_summaries.serialize_json(
                value["workload_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWorkloadsOutput:
    out: ListWorkloadsOutput = {}  # type: ignore[typeddict-item]
    if "WorkloadSummaries" in data:
        import aws_sdk_wellarchitected.types.workload_summaries

        out["workload_summaries"] = (
            aws_sdk_wellarchitected.types.workload_summaries.deserialize_json(
                data["WorkloadSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
