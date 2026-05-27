"""Generated from Smithy shape ``com.amazonaws.eks#DeleteFargateProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.string


class DeleteFargateProfileRequest(TypedDict):
    cluster_name: "aws_sdk_eks.types.string.String"
    """<p>The name of your cluster.</p>"""
    fargate_profile_name: "aws_sdk_eks.types.string.String"
    """<p>The name of the Fargate profile to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFargateProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFargateProfileRequest:
    out: DeleteFargateProfileRequest = {}  # type: ignore[typeddict-item]
    return out
