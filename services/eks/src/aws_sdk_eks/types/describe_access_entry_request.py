"""Generated from Smithy shape ``com.amazonaws.eks#DescribeAccessEntryRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.string


class DescribeAccessEntryRequest(TypedDict):
    cluster_name: "aws_sdk_eks.types.string.String"
    """<p>The name of your cluster.</p>"""
    principal_arn: "aws_sdk_eks.types.string.String"
    """<p>The ARN of the IAM principal for the <code>AccessEntry</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAccessEntryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAccessEntryRequest:
    out: DescribeAccessEntryRequest = {}  # type: ignore[typeddict-item]
    return out
