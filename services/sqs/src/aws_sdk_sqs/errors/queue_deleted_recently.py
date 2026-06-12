"""Generated from Smithy shape ``com.amazonaws.sqs#QueueDeletedRecently``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sqs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sqs.types.exception_message


class QueueDeletedRecently_(TypedDict):
    message: NotRequired["aws_sdk_sqs.types.exception_message.ExceptionMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: QueueDeletedRecently_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> QueueDeletedRecently_:
    out: QueueDeletedRecently_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class QueueDeletedRecently(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sqs#QueueDeletedRecently``."""

    code: str | None = "QueueDeletedRecently"

    def __init__(self, data: QueueDeletedRecently_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="QueueDeletedRecently",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "QueueDeletedRecently":
        return cls(deserialize_aws_json_1_0(data))
