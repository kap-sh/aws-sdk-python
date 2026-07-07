"""Generated from Smithy shape ``com.amazonaws.eks#DescribeClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.string


class DescribeClusterRequest(TypedDict, closed=True):
    name: "aws_sdk_eks.types.string.String"
    """<p>The name of your cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeClusterRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeClusterRequest:
    out: DescribeClusterRequest = {}  # type: ignore[typeddict-item]
    return out
