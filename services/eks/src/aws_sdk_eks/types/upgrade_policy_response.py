"""Generated from Smithy shape ``com.amazonaws.eks#UpgradePolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.support_type


class UpgradePolicyResponse(TypedDict):
    support_type: NotRequired["aws_sdk_eks.types.support_type.SupportType"]
    """<p>If the cluster is set to <code>EXTENDED</code>, it will enter extended support at the end of standard support. If the cluster is set to <code>STANDARD</code>, it will be automatically upgraded at the end of standard support.</p> <p> <a href=\"https://docs.aws.amazon.com/eks/latest/userguide/extended-support-control.html\">Learn more about EKS Extended Support in the <i>Amazon EKS User Guide</i>.</a> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpgradePolicyResponse) -> dict:
    out: dict = {}
    if "support_type" in value:
        import aws_sdk_eks.types.support_type

        out["supportType"] = aws_sdk_eks.types.support_type.serialize_json(
            value["support_type"]
        )
    return out


def deserialize_json(data: dict) -> UpgradePolicyResponse:
    out: UpgradePolicyResponse = {}  # type: ignore[typeddict-item]
    if "supportType" in data:
        import aws_sdk_eks.types.support_type

        out["support_type"] = aws_sdk_eks.types.support_type.deserialize_json(
            data["supportType"]
        )
    return out
