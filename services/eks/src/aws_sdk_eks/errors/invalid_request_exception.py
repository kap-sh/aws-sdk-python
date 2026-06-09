"""Generated from Smithy shape ``com.amazonaws.eks#InvalidRequestException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_eks.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_eks.types.string


class InvalidRequestException_(TypedDict):
    cluster_name: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Amazon EKS cluster associated with the exception.</p>"""
    nodegroup_name: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Amazon EKS managed node group associated with the exception.</p>"""
    addon_name: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The request is invalid given the state of the add-on name. Check the state of the cluster and the associated operations.</p>"""
    subscription_id: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Amazon EKS subscription ID with the exception.</p>"""
    message: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Amazon EKS add-on name associated with the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidRequestException_) -> dict:
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


def deserialize_json(data: dict) -> InvalidRequestException_:
    out: InvalidRequestException_ = {}  # type: ignore[typeddict-item]
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


class InvalidRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.eks#InvalidRequestException``."""

    code: str | None = "InvalidRequestException"

    def __init__(self, data: InvalidRequestException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidRequestException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidRequestException":
        return cls(deserialize_json(data))
