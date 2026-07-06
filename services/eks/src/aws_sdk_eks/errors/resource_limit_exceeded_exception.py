"""Generated from Smithy shape ``com.amazonaws.eks#ResourceLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_eks.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_eks.types.string


class ResourceLimitExceededException_(TypedDict, closed=True):
    cluster_name: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Amazon EKS cluster associated with the exception.</p>"""
    nodegroup_name: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Amazon EKS managed node group associated with the exception.</p>"""
    subscription_id: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Amazon EKS subscription ID with the exception.</p>"""
    message: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Amazon EKS message associated with the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceLimitExceededException_) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "nodegroup_name" in value:
        out["nodegroupName"] = value["nodegroup_name"]
    if "subscription_id" in value:
        out["subscriptionId"] = value["subscription_id"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceLimitExceededException_:
    out: ResourceLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "clusterName" in data:
        out["cluster_name"] = data["clusterName"]
    if "nodegroupName" in data:
        out["nodegroup_name"] = data["nodegroupName"]
    if "subscriptionId" in data:
        out["subscription_id"] = data["subscriptionId"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ResourceLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.eks#ResourceLimitExceededException``."""

    code: str | None = "ResourceLimitExceededException"

    def __init__(self, data: ResourceLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceLimitExceededException":
        return cls(deserialize_json(data))
