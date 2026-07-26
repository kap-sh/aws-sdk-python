"""Generated from Smithy shape ``com.amazonaws.memorydb#ClusterNotFoundFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_memorydb.errors import ServiceError

if TYPE_CHECKING:
    import capo_memorydb.types.exception_message


class ClusterNotFoundFault_(TypedDict, closed=True):
    message: NotRequired["capo_memorydb.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterNotFoundFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterNotFoundFault_:
    out: ClusterNotFoundFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ClusterNotFoundFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.memorydb#ClusterNotFoundFault``."""

    code: str | None = "ClusterNotFoundFault"

    def __init__(self, data: ClusterNotFoundFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ClusterNotFoundFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ClusterNotFoundFault":
        return cls(deserialize_aws_json_1_1(data))
