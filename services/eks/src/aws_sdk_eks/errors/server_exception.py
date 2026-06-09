"""Generated from Smithy shape ``com.amazonaws.eks#ServerException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_eks.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_eks.types.string


class ServerException_(TypedDict):
    cluster_name: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Amazon EKS cluster associated with the exception.</p>"""
    nodegroup_name: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Amazon EKS managed node group associated with the exception.</p>"""
    addon_name: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Amazon EKS add-on name associated with the exception.</p>"""
    subscription_id: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Amazon EKS subscription ID with the exception.</p>"""
    message: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>These errors are usually caused by a server-side issue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServerException_) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "nodegroup_name" in value:
        out["nodegroupName"] = value["nodegroup_name"]
    if "addon_name" in value:
        out["addonName"] = value["addon_name"]
    if "subscription_id" in value:
        out["subscriptionId"] = value["subscription_id"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ServerException_:
    out: ServerException_ = {}  # type: ignore[typeddict-item]
    if "clusterName" in data:
        out["cluster_name"] = data["clusterName"]
    if "nodegroupName" in data:
        out["nodegroup_name"] = data["nodegroupName"]
    if "addonName" in data:
        out["addon_name"] = data["addonName"]
    if "subscriptionId" in data:
        out["subscription_id"] = data["subscriptionId"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.eks#ServerException``."""

    code: str | None = "ServerException"

    def __init__(self, data: ServerException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServerException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ServerException":
        return cls(deserialize_json(data))
