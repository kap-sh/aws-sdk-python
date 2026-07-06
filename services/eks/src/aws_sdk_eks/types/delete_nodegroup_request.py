"""Generated from Smithy shape ``com.amazonaws.eks#DeleteNodegroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.string


class DeleteNodegroupRequest(TypedDict, closed=True):
    cluster_name: "aws_sdk_eks.types.string.String"
    """<p>The name of your cluster.</p>"""
    nodegroup_name: "aws_sdk_eks.types.string.String"
    """<p>The name of the node group to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteNodegroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteNodegroupRequest:
    out: DeleteNodegroupRequest = {}  # type: ignore[typeddict-item]
    return out
