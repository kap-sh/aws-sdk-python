"""Generated from Smithy shape ``com.amazonaws.eks#DescribeInsightRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.string


class DescribeInsightRequest(TypedDict, closed=True):
    cluster_name: "aws_sdk_eks.types.string.String"
    """<p>The name of the cluster to describe the insight for.</p>"""
    id: "aws_sdk_eks.types.string.String"
    """<p>The identity of the insight to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeInsightRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeInsightRequest:
    out: DescribeInsightRequest = {}  # type: ignore[typeddict-item]
    return out
