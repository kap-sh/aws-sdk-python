"""Generated from Smithy shape ``com.amazonaws.memorydb#InvalidParameterGroupStateFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_memorydb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.exception_message


class InvalidParameterGroupStateFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_memorydb.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidParameterGroupStateFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidParameterGroupStateFault_:
    out: InvalidParameterGroupStateFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidParameterGroupStateFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.memorydb#InvalidParameterGroupStateFault``."""

    code: str | None = "InvalidParameterGroupStateFault"

    def __init__(self, data: InvalidParameterGroupStateFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidParameterGroupStateFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidParameterGroupStateFault":
        return cls(deserialize_aws_json_1_1(data))
