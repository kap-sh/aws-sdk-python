"""Generated from Smithy shape ``com.amazonaws.eks#DeregisterClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string


class DeregisterClusterRequest(TypedDict, closed=True):
    name: "capo_eks.types.string.String"
    """<p>The name of the connected cluster to deregister.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterClusterRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeregisterClusterRequest:
    out: DeregisterClusterRequest = {}  # type: ignore[typeddict-item]
    return out
