"""Generated from Smithy shape ``com.amazonaws.sqs#QueueDoesNotExist``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sqs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sqs.types.exception_message


class QueueDoesNotExist_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_sqs.types.exception_message.ExceptionMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: QueueDoesNotExist_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> QueueDoesNotExist_:
    out: QueueDoesNotExist_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class QueueDoesNotExist(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sqs#QueueDoesNotExist``."""

    code: str | None = "QueueDoesNotExist"

    def __init__(self, data: QueueDoesNotExist_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="QueueDoesNotExist",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "QueueDoesNotExist":
        return cls(deserialize_aws_json_1_0(data))
