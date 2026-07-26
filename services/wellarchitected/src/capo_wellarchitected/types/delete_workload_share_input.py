"""Generated from Smithy shape ``com.amazonaws.wellarchitected#DeleteWorkloadShareInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.client_request_token
    import capo_wellarchitected.types.share_id
    import capo_wellarchitected.types.workload_id


class DeleteWorkloadShareInput(TypedDict, closed=True):
    share_id: "capo_wellarchitected.types.share_id.ShareId"
    workload_id: "capo_wellarchitected.types.workload_id.WorkloadId"
    client_request_token: NotRequired[
        "capo_wellarchitected.types.client_request_token.ClientRequestToken"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkloadShareInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWorkloadShareInput:
    out: DeleteWorkloadShareInput = {}  # type: ignore[typeddict-item]
    return out
