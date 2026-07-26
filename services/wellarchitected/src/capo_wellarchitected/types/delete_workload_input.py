"""Generated from Smithy shape ``com.amazonaws.wellarchitected#DeleteWorkloadInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.client_request_token
    import capo_wellarchitected.types.workload_id


class DeleteWorkloadInput(TypedDict, closed=True):
    workload_id: "capo_wellarchitected.types.workload_id.WorkloadId"
    client_request_token: NotRequired[
        "capo_wellarchitected.types.client_request_token.ClientRequestToken"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkloadInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWorkloadInput:
    out: DeleteWorkloadInput = {}  # type: ignore[typeddict-item]
    return out
