"""Generated from Smithy shape ``com.amazonaws.eks#DescribeFargateProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string


class DescribeFargateProfileRequest(TypedDict, closed=True):
    cluster_name: "capo_eks.types.string.String"
    """<p>The name of your cluster.</p>"""
    fargate_profile_name: "capo_eks.types.string.String"
    """<p>The name of the Fargate profile to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFargateProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeFargateProfileRequest:
    out: DescribeFargateProfileRequest = {}  # type: ignore[typeddict-item]
    return out
