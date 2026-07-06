"""Generated from Smithy shape ``com.amazonaws.eksauth#PodIdentityAssociation``."""

from typing_extensions import TypedDict

from aws_sdk_eks_auth.errors import DeserializationError


class PodIdentityAssociation(TypedDict, closed=True):
    association_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the EKS Pod Identity association.</p>"""
    association_id: "str"
    """<p>The ID of the association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PodIdentityAssociation) -> dict:
    out: dict = {}
    out["associationArn"] = value["association_arn"]
    out["associationId"] = value["association_id"]
    return out


def deserialize_json(data: dict) -> PodIdentityAssociation:
    out: PodIdentityAssociation = {}  # type: ignore[typeddict-item]
    if "associationArn" in data:
        out["association_arn"] = data["associationArn"]
    else:
        raise DeserializationError("PodIdentityAssociation.association_arn required")
    if "associationId" in data:
        out["association_id"] = data["associationId"]
    else:
        raise DeserializationError("PodIdentityAssociation.association_id required")
    return out
