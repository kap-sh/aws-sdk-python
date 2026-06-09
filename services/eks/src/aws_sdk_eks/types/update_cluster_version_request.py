"""Generated from Smithy shape ``com.amazonaws.eks#UpdateClusterVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_eks.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eks.types.boolean
    import aws_sdk_eks.types.string


class UpdateClusterVersionRequest(TypedDict):
    name: "aws_sdk_eks.types.string.String"
    """<p>The name of the Amazon EKS cluster to update.</p>"""
    version: "aws_sdk_eks.types.string.String"
    """<p>The desired Kubernetes version following a successful update.</p>"""
    client_request_token: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    force: "aws_sdk_eks.types.boolean.Boolean"
    """<p>Set this value to <code>true</code> to override upgrade-blocking readiness checks when updating a cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateClusterVersionRequest) -> dict:
    out: dict = {}
    out["version"] = value["version"]
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    out["force"] = value.get("force", False)
    return out


def deserialize_json(data: dict) -> UpdateClusterVersionRequest:
    out: UpdateClusterVersionRequest = {}  # type: ignore[typeddict-item]
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("UpdateClusterVersionRequest.version required")
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    if "force" in data:
        out["force"] = data["force"]
    else:
        out["force"] = False
    return out
