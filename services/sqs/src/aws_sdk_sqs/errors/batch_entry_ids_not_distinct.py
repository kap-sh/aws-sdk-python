"""Generated from Smithy shape ``com.amazonaws.sqs#BatchEntryIdsNotDistinct``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sqs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sqs.types.exception_message


class BatchEntryIdsNotDistinct_(TypedDict):
    message: NotRequired["aws_sdk_sqs.types.exception_message.ExceptionMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchEntryIdsNotDistinct_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchEntryIdsNotDistinct_:
    out: BatchEntryIdsNotDistinct_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class BatchEntryIdsNotDistinct(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sqs#BatchEntryIdsNotDistinct``."""

    code: str | None = "BatchEntryIdsNotDistinct"

    def __init__(self, data: BatchEntryIdsNotDistinct_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BatchEntryIdsNotDistinct",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "BatchEntryIdsNotDistinct":
        return cls(deserialize_aws_json_1_0(data))
