"""Generated from Smithy shape ``com.amazonaws.eks#DeregisterClusterRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.string


class DeregisterClusterRequest(TypedDict):
    name: "aws_sdk_eks.types.string.String"
    """<p>The name of the connected cluster to deregister.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterClusterRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeregisterClusterRequest:
    out: DeregisterClusterRequest = {}  # type: ignore[typeddict-item]
    return out
