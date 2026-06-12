"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListProfileNotificationsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.max_results
    import aws_sdk_wellarchitected.types.next_token
    import aws_sdk_wellarchitected.types.workload_id


class ListProfileNotificationsInput(TypedDict):
    workload_id: NotRequired["aws_sdk_wellarchitected.types.workload_id.WorkloadId"]
    next_token: NotRequired["aws_sdk_wellarchitected.types.next_token.NextToken"]
    max_results: NotRequired["aws_sdk_wellarchitected.types.max_results.MaxResults"]


# --- restJson1 ser/de ---
def serialize_json(value: ListProfileNotificationsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListProfileNotificationsInput:
    out: ListProfileNotificationsInput = {}  # type: ignore[typeddict-item]
    return out
