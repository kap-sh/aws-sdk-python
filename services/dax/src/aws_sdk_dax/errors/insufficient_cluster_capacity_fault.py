"""Generated from Smithy shape ``com.amazonaws.dax#InsufficientClusterCapacityFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dax.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dax.types.exception_message


class InsufficientClusterCapacityFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_dax.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InsufficientClusterCapacityFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InsufficientClusterCapacityFault_:
    out: InsufficientClusterCapacityFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InsufficientClusterCapacityFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dax#InsufficientClusterCapacityFault``."""

    code: str | None = "InsufficientClusterCapacityFault"

    def __init__(self, data: InsufficientClusterCapacityFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InsufficientClusterCapacityFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InsufficientClusterCapacityFault":
        return cls(deserialize_aws_json_1_1(data))
