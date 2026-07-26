"""Generated from Smithy shape ``com.amazonaws.eks#AddonPodIdentityAssociations``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_eks.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eks.types.string


class AddonPodIdentityAssociations(TypedDict, closed=True):
    service_account: "capo_eks.types.string.String"
    """<p>The name of a Kubernetes Service Account.</p>"""
    role_arn: "capo_eks.types.string.String"
    """<p>The ARN of an IAM Role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddonPodIdentityAssociations) -> dict:
    out: dict = {}
    out["serviceAccount"] = value["service_account"]
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> AddonPodIdentityAssociations:
    out: AddonPodIdentityAssociations = {}  # type: ignore[typeddict-item]
    if "serviceAccount" in data:
        out["service_account"] = data["serviceAccount"]
    else:
        raise DeserializationError(
            "AddonPodIdentityAssociations.service_account required"
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("AddonPodIdentityAssociations.role_arn required")
    return out
