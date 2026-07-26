"""Generated from Smithy shape ``com.amazonaws.eks#DescribeCapabilityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string


class DescribeCapabilityRequest(TypedDict, closed=True):
    cluster_name: "capo_eks.types.string.String"
    """<p>The name of the Amazon EKS cluster that contains the capability you want to describe.</p>"""
    capability_name: "capo_eks.types.string.String"
    """<p>The name of the capability to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCapabilityRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeCapabilityRequest:
    out: DescribeCapabilityRequest = {}  # type: ignore[typeddict-item]
    return out
