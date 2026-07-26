"""Generated from Smithy shape ``com.amazonaws.medialive#DeleteNodeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class DeleteNodeRequest(TypedDict, closed=True):
    cluster_id: "capo_medialive.types.__string.__string"
    """The ID of the cluster"""
    node_id: "capo_medialive.types.__string.__string"
    """The ID of the node."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteNodeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteNodeRequest:
    out: DeleteNodeRequest = {}  # type: ignore[typeddict-item]
    return out
