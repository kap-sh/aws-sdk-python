"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DeleteDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.id


class DeleteDatasetRequest(TypedDict, closed=True):
    dataset_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the dataset.</p>"""
    client_token: NotRequired["capo_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDatasetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDatasetRequest:
    out: DeleteDatasetRequest = {}  # type: ignore[typeddict-item]
    return out
