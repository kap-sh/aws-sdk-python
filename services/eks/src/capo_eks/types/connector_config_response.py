"""Generated from Smithy shape ``com.amazonaws.eks#ConnectorConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string
    import capo_eks.types.timestamp


class ConnectorConfigResponse(TypedDict, closed=True):
    activation_id: NotRequired["capo_eks.types.string.String"]
    """<p>A unique ID associated with the cluster for registration purposes.</p>"""
    activation_code: NotRequired["capo_eks.types.string.String"]
    """<p>A unique code associated with the cluster for registration purposes.</p>"""
    activation_expiry: NotRequired["capo_eks.types.timestamp.Timestamp"]
    """<p>The expiration time of the connected cluster. The cluster's YAML file must be applied through the native provider.</p>"""
    provider: NotRequired["capo_eks.types.string.String"]
    """<p>The cluster's cloud service provider.</p>"""
    role_arn: NotRequired["capo_eks.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the role to communicate with services from the connected Kubernetes cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorConfigResponse) -> dict:
    out: dict = {}
    if "activation_id" in value:
        out["activationId"] = value["activation_id"]
    if "activation_code" in value:
        out["activationCode"] = value["activation_code"]
    if "activation_expiry" in value:
        import capo_eks.types.timestamp

        out["activationExpiry"] = capo_eks.types.timestamp.serialize_json(
            value["activation_expiry"]
        )
    if "provider" in value:
        out["provider"] = value["provider"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> ConnectorConfigResponse:
    out: ConnectorConfigResponse = {}  # type: ignore[typeddict-item]
    if "activationId" in data:
        out["activation_id"] = data["activationId"]
    if "activationCode" in data:
        out["activation_code"] = data["activationCode"]
    if "activationExpiry" in data:
        import capo_eks.types.timestamp

        out["activation_expiry"] = capo_eks.types.timestamp.deserialize_json(
            data["activationExpiry"]
        )
    if "provider" in data:
        out["provider"] = data["provider"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    return out
