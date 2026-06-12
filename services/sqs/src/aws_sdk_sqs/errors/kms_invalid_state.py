"""Generated from Smithy shape ``com.amazonaws.sqs#KmsInvalidState``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sqs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sqs.types.exception_message


class KmsInvalidState_(TypedDict):
    message: NotRequired["aws_sdk_sqs.types.exception_message.ExceptionMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KmsInvalidState_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> KmsInvalidState_:
    out: KmsInvalidState_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class KmsInvalidState(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sqs#KmsInvalidState``."""

    code: str | None = "KmsInvalidState"

    def __init__(self, data: KmsInvalidState_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="KmsInvalidState",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "KmsInvalidState":
        return cls(deserialize_aws_json_1_0(data))
