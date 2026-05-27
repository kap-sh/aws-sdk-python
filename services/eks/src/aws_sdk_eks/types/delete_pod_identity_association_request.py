"""Generated from Smithy shape ``com.amazonaws.eks#DeletePodIdentityAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.string


class DeletePodIdentityAssociationRequest(TypedDict):
    cluster_name: "aws_sdk_eks.types.string.String"
    """<p>The cluster name that</p>"""
    association_id: "aws_sdk_eks.types.string.String"
    """<p>The ID of the association to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePodIdentityAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePodIdentityAssociationRequest:
    out: DeletePodIdentityAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
