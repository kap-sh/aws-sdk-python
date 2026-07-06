"""Generated from Smithy shape ``com.amazonaws.eks#DeleteCapabilityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.string


class DeleteCapabilityRequest(TypedDict, closed=True):
    cluster_name: "aws_sdk_eks.types.string.String"
    """<p>The name of the Amazon EKS cluster that contains the capability you want to delete.</p>"""
    capability_name: "aws_sdk_eks.types.string.String"
    """<p>The name of the capability to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCapabilityRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCapabilityRequest:
    out: DeleteCapabilityRequest = {}  # type: ignore[typeddict-item]
    return out
