"""Generated from Smithy shape ``com.amazonaws.eks#DescribePodIdentityAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string


class DescribePodIdentityAssociationRequest(TypedDict, closed=True):
    cluster_name: "capo_eks.types.string.String"
    """<p>The name of the cluster that the association is in.</p>"""
    association_id: "capo_eks.types.string.String"
    """<p>The ID of the association that you want the description of.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePodIdentityAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribePodIdentityAssociationRequest:
    out: DescribePodIdentityAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
