"""Generated from Smithy shape ``com.amazonaws.eks#FargateProfileSelector``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.fargate_profile_label
    import aws_sdk_eks.types.string


class FargateProfileSelector(TypedDict):
    namespace: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Kubernetes <code>namespace</code> that the selector should match.</p>"""
    labels: NotRequired["aws_sdk_eks.types.fargate_profile_label.FargateProfileLabel"]
    """<p>The Kubernetes labels that the selector should match. A pod must contain all of the labels that are specified in the selector for it to be considered a match.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FargateProfileSelector) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "labels" in value:
        import aws_sdk_eks.types.fargate_profile_label

        out["labels"] = aws_sdk_eks.types.fargate_profile_label.serialize_json(
            value["labels"]
        )
    return out


def deserialize_json(data: dict) -> FargateProfileSelector:
    out: FargateProfileSelector = {}  # type: ignore[typeddict-item]
    if "namespace" in data:
        out["namespace"] = data["namespace"]
    if "labels" in data:
        import aws_sdk_eks.types.fargate_profile_label

        out["labels"] = aws_sdk_eks.types.fargate_profile_label.deserialize_json(
            data["labels"]
        )
    return out
