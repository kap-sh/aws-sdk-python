"""Generated from Smithy shape ``com.amazonaws.eks#DeleteClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string


class DeleteClusterRequest(TypedDict, closed=True):
    name: "capo_eks.types.string.String"
    """<p>The name of the cluster to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteClusterRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteClusterRequest:
    out: DeleteClusterRequest = {}  # type: ignore[typeddict-item]
    return out
