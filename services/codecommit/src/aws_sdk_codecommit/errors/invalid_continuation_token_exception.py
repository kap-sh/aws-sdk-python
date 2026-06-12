"""Generated from Smithy shape ``com.amazonaws.codecommit#InvalidContinuationTokenException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codecommit.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.message


class InvalidContinuationTokenException_(TypedDict):
    message: NotRequired["aws_sdk_codecommit.types.message.Message"]
    """<p>Any message associated with the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidContinuationTokenException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidContinuationTokenException_:
    out: InvalidContinuationTokenException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidContinuationTokenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codecommit#InvalidContinuationTokenException``."""

    code: str | None = "InvalidContinuationTokenException"

    def __init__(self, data: InvalidContinuationTokenException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidContinuationTokenException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidContinuationTokenException":
        return cls(deserialize_aws_json_1_1(data))
