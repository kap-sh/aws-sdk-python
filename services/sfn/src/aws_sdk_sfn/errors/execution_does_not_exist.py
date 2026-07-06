"""Generated from Smithy shape ``com.amazonaws.sfn#ExecutionDoesNotExist``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sfn.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.error_message


class ExecutionDoesNotExist_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_sfn.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecutionDoesNotExist_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ExecutionDoesNotExist_:
    out: ExecutionDoesNotExist_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ExecutionDoesNotExist(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sfn#ExecutionDoesNotExist``."""

    code: str | None = "ExecutionDoesNotExist"

    def __init__(self, data: ExecutionDoesNotExist_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ExecutionDoesNotExist",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "ExecutionDoesNotExist":
        return cls(deserialize_aws_json_1_0(data))
