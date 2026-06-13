"""Generated from Smithy shape ``com.amazonaws.eksauth#AssumeRoleForPodIdentityRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_eks_auth.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eks_auth.types.cluster_name
    import aws_sdk_eks_auth.types.jwt_token


class AssumeRoleForPodIdentityRequest(TypedDict):
    cluster_name: "aws_sdk_eks_auth.types.cluster_name.ClusterName"
    """<p>The name of the cluster for the request.</p>"""
    token: "aws_sdk_eks_auth.types.jwt_token.JwtToken"
    """<p>The token of the Kubernetes service account for the pod.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssumeRoleForPodIdentityRequest) -> dict:
    out: dict = {}
    out["token"] = value["token"]
    return out


def deserialize_json(data: dict) -> AssumeRoleForPodIdentityRequest:
    out: AssumeRoleForPodIdentityRequest = {}  # type: ignore[typeddict-item]
    if "token" in data:
        out["token"] = data["token"]
    else:
        raise DeserializationError("AssumeRoleForPodIdentityRequest.token required")
    return out
