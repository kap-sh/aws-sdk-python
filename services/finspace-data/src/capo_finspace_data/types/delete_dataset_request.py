"""Generated from Smithy shape ``com.amazonaws.finspacedata#DeleteDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace_data.types.client_token
    import capo_finspace_data.types.dataset_id


class DeleteDatasetRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_finspace_data.types.client_token.ClientToken"]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""
    dataset_id: "capo_finspace_data.types.dataset_id.DatasetId"
    """<p>The unique identifier of the Dataset to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDatasetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDatasetRequest:
    out: DeleteDatasetRequest = {}  # type: ignore[typeddict-item]
    return out
