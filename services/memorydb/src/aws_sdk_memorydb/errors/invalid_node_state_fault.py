"""Generated from Smithy shape ``com.amazonaws.memorydb#InvalidNodeStateFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_memorydb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.exception_message


class InvalidNodeStateFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_memorydb.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidNodeStateFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidNodeStateFault_:
    out: InvalidNodeStateFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidNodeStateFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.memorydb#InvalidNodeStateFault``."""

    code: str | None = "InvalidNodeStateFault"

    def __init__(self, data: InvalidNodeStateFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidNodeStateFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidNodeStateFault":
        return cls(deserialize_aws_json_1_1(data))
