"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListWorkloadSharesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.list_workload_shares_max_results
    import aws_sdk_wellarchitected.types.next_token
    import aws_sdk_wellarchitected.types.share_status
    import aws_sdk_wellarchitected.types.shared_with_prefix
    import aws_sdk_wellarchitected.types.workload_id


class ListWorkloadSharesInput(TypedDict, closed=True):
    workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId"
    shared_with_prefix: NotRequired[
        "aws_sdk_wellarchitected.types.shared_with_prefix.SharedWithPrefix"
    ]
    """<p>The Amazon Web Services account ID, organization ID, or organizational unit (OU) ID with which the workload is shared.</p>"""
    next_token: NotRequired["aws_sdk_wellarchitected.types.next_token.NextToken"]
    max_results: NotRequired[
        "aws_sdk_wellarchitected.types.list_workload_shares_max_results.ListWorkloadSharesMaxResults"
    ]
    """<p>The maximum number of results to return for this request.</p>"""
    status: NotRequired["aws_sdk_wellarchitected.types.share_status.ShareStatus"]


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkloadSharesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListWorkloadSharesInput:
    out: ListWorkloadSharesInput = {}  # type: ignore[typeddict-item]
    return out
