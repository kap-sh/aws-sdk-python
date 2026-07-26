"""Generated from Smithy shape ``com.amazonaws.dax#NodeNotFoundFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dax.errors import ServiceError

if TYPE_CHECKING:
    import capo_dax.types.exception_message


class NodeNotFoundFault_(TypedDict, closed=True):
    message: NotRequired["capo_dax.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NodeNotFoundFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NodeNotFoundFault_:
    out: NodeNotFoundFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class NodeNotFoundFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dax#NodeNotFoundFault``."""

    code: str | None = "NodeNotFoundFault"

    def __init__(self, data: NodeNotFoundFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NodeNotFoundFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "NodeNotFoundFault":
        return cls(deserialize_aws_json_1_1(data))
