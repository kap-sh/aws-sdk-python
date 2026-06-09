"""Generated from Smithy shape ``com.amazonaws.eks#DescribePodIdentityAssociationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.pod_identity_association


class DescribePodIdentityAssociationResponse(TypedDict):
    association: NotRequired[
        "aws_sdk_eks.types.pod_identity_association.PodIdentityAssociation"
    ]
    """<p>The full description of the EKS Pod Identity association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePodIdentityAssociationResponse) -> dict:
    out: dict = {}
    if "association" in value:
        import aws_sdk_eks.types.pod_identity_association

        out["association"] = aws_sdk_eks.types.pod_identity_association.serialize_json(
            value["association"]
        )
    return out


def deserialize_json(data: dict) -> DescribePodIdentityAssociationResponse:
    out: DescribePodIdentityAssociationResponse = {}  # type: ignore[typeddict-item]
    if "association" in data:
        import aws_sdk_eks.types.pod_identity_association

        out["association"] = (
            aws_sdk_eks.types.pod_identity_association.deserialize_json(
                data["association"]
            )
        )
    return out
