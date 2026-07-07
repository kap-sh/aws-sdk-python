"""Generated from Smithy shape ``com.amazonaws.firehose#InvalidArgumentException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_firehose.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_firehose.types.error_message


class InvalidArgumentException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_firehose.types.error_message.ErrorMessage"]
    """<p>A message that provides information about the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidArgumentException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidArgumentException_:
    out: InvalidArgumentException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidArgumentException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.firehose#InvalidArgumentException``."""

    code: str | None = "InvalidArgumentException"

    def __init__(self, data: InvalidArgumentException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidArgumentException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidArgumentException":
        return cls(deserialize_aws_json_1_1(data))
