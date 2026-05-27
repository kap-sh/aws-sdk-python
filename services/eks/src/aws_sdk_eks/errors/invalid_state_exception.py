"""Generated from Smithy shape ``com.amazonaws.eks#InvalidStateException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_eks.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_eks.types.string


class InvalidStateException_(TypedDict):
    cluster_name: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Amazon EKS cluster associated with the exception.</p>"""
    message: NotRequired["aws_sdk_eks.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidStateException_) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidStateException_:
    out: InvalidStateException_ = {}  # type: ignore[typeddict-item]
    if "clusterName" in data:
        out["cluster_name"] = data["clusterName"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.eks#InvalidStateException``."""

    code: str | None = "InvalidStateException"

    def __init__(self, data: InvalidStateException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidStateException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidStateException":
        return cls(deserialize_json(data))
