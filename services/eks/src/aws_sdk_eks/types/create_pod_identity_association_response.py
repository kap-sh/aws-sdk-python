"""Generated from Smithy shape ``com.amazonaws.eks#CreatePodIdentityAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.pod_identity_association


class CreatePodIdentityAssociationResponse(TypedDict, closed=True):
    association: NotRequired[
        "aws_sdk_eks.types.pod_identity_association.PodIdentityAssociation"
    ]
    """<p>The full description of your new association.</p> <p>The description includes an ID for the association. Use the ID of the association in further actions to manage the association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePodIdentityAssociationResponse) -> dict:
    out: dict = {}
    if "association" in value:
        import aws_sdk_eks.types.pod_identity_association

        out["association"] = aws_sdk_eks.types.pod_identity_association.serialize_json(
            value["association"]
        )
    return out


def deserialize_json(data: dict) -> CreatePodIdentityAssociationResponse:
    out: CreatePodIdentityAssociationResponse = {}  # type: ignore[typeddict-item]
    if "association" in data:
        import aws_sdk_eks.types.pod_identity_association

        out["association"] = (
            aws_sdk_eks.types.pod_identity_association.deserialize_json(
                data["association"]
            )
        )
    return out
