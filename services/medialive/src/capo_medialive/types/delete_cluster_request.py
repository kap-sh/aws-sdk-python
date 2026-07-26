"""Generated from Smithy shape ``com.amazonaws.medialive#DeleteClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class DeleteClusterRequest(TypedDict, closed=True):
    cluster_id: "capo_medialive.types.__string.__string"
    """The ID of the cluster."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteClusterRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteClusterRequest:
    out: DeleteClusterRequest = {}  # type: ignore[typeddict-item]
    return out
