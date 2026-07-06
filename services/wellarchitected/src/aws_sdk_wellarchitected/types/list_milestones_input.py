"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListMilestonesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.max_results
    import aws_sdk_wellarchitected.types.next_token
    import aws_sdk_wellarchitected.types.workload_id


class ListMilestonesInput(TypedDict, closed=True):
    workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId"
    next_token: NotRequired["aws_sdk_wellarchitected.types.next_token.NextToken"]
    max_results: NotRequired["aws_sdk_wellarchitected.types.max_results.MaxResults"]


# --- restJson1 ser/de ---
def serialize_json(value: ListMilestonesInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListMilestonesInput:
    out: ListMilestonesInput = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
