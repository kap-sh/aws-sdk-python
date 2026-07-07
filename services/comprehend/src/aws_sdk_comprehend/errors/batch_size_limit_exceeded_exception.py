"""Generated from Smithy shape ``com.amazonaws.comprehend#BatchSizeLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_comprehend.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.string


class BatchSizeLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_comprehend.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchSizeLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchSizeLimitExceededException_:
    out: BatchSizeLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class BatchSizeLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.comprehend#BatchSizeLimitExceededException``."""

    code: str | None = "BatchSizeLimitExceededException"

    def __init__(self, data: BatchSizeLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BatchSizeLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "BatchSizeLimitExceededException":
        return cls(deserialize_aws_json_1_1(data))
