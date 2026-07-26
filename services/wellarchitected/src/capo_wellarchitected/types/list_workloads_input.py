"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListWorkloadsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.list_workloads_max_results
    import capo_wellarchitected.types.next_token
    import capo_wellarchitected.types.workload_name_prefix


class ListWorkloadsInput(TypedDict, closed=True):
    workload_name_prefix: NotRequired[
        "capo_wellarchitected.types.workload_name_prefix.WorkloadNamePrefix"
    ]
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]
    max_results: NotRequired[
        "capo_wellarchitected.types.list_workloads_max_results.ListWorkloadsMaxResults"
    ]
    """<p>The maximum number of results to return for this request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkloadsInput) -> dict:
    out: dict = {}
    if "workload_name_prefix" in value:
        out["WorkloadNamePrefix"] = value["workload_name_prefix"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListWorkloadsInput:
    out: ListWorkloadsInput = {}  # type: ignore[typeddict-item]
    if "WorkloadNamePrefix" in data:
        out["workload_name_prefix"] = data["WorkloadNamePrefix"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
