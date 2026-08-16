"""Generated from Smithy shape ``com.amazonaws.sqs#KmsThrottled``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sqs.errors import ServiceError

if TYPE_CHECKING:
    import capo_sqs.types.exception_message


class KmsThrottled_(TypedDict, closed=True):
    message: NotRequired["capo_sqs.types.exception_message.ExceptionMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KmsThrottled_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> KmsThrottled_:
    out: KmsThrottled_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class KmsThrottled(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sqs#KmsThrottled``."""

    code: str | None = "KmsThrottled"

    def __init__(self, data: KmsThrottled_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="KmsThrottled",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None
    ) -> "KmsThrottled":
        return cls(deserialize_aws_json_1_0(data), message)
