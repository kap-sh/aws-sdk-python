"""Generated from Smithy shape ``com.amazonaws.eks#UnsupportedAvailabilityZoneException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_eks.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.string_list


class UnsupportedAvailabilityZoneException_(TypedDict):
    message: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>At least one of your specified cluster subnets is in an Availability Zone that does not support Amazon EKS. The exception output specifies the supported Availability Zones for your account, from which you can choose subnets for your cluster.</p>"""
    cluster_name: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Amazon EKS cluster associated with the exception.</p>"""
    nodegroup_name: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Amazon EKS managed node group associated with the exception.</p>"""
    valid_zones: NotRequired["aws_sdk_eks.types.string_list.StringList"]
    """<p>The supported Availability Zones for your account. Choose subnets in these Availability Zones for your cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnsupportedAvailabilityZoneException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "nodegroup_name" in value:
        out["nodegroupName"] = value["nodegroup_name"]
    if "valid_zones" in value:
        import aws_sdk_eks.types.string_list

        out["validZones"] = aws_sdk_eks.types.string_list.serialize_json(
            value["valid_zones"]
        )
    return out


def deserialize_json(data: dict) -> UnsupportedAvailabilityZoneException_:
    out: UnsupportedAvailabilityZoneException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "clusterName" in data:
        out["cluster_name"] = data["clusterName"]
    if "nodegroupName" in data:
        out["nodegroup_name"] = data["nodegroupName"]
    if "validZones" in data:
        import aws_sdk_eks.types.string_list

        out["valid_zones"] = aws_sdk_eks.types.string_list.deserialize_json(
            data["validZones"]
        )
    return out


class UnsupportedAvailabilityZoneException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.eks#UnsupportedAvailabilityZoneException``."""

    code: str | None = "UnsupportedAvailabilityZoneException"

    def __init__(self, data: UnsupportedAvailabilityZoneException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedAvailabilityZoneException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "UnsupportedAvailabilityZoneException":
        return cls(deserialize_json(data))
