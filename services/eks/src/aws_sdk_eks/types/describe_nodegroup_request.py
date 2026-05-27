"""Generated from Smithy shape ``com.amazonaws.eks#DescribeNodegroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.string


class DescribeNodegroupRequest(TypedDict):
    cluster_name: "aws_sdk_eks.types.string.String"
    """<p>The name of your cluster.</p>"""
    nodegroup_name: "aws_sdk_eks.types.string.String"
    """<p>The name of the node group to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeNodegroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeNodegroupRequest:
    out: DescribeNodegroupRequest = {}  # type: ignore[typeddict-item]
    return out
