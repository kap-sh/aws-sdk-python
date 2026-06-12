"""Generated from Smithy shape ``com.amazonaws.cloudtrail#InvalidS3PrefixException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudtrail.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.error_message


class InvalidS3PrefixException_(TypedDict):
    message: NotRequired["aws_sdk_cloudtrail.types.error_message.ErrorMessage"]
    """<p>Brief description of the exception returned by the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidS3PrefixException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidS3PrefixException_:
    out: InvalidS3PrefixException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidS3PrefixException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudtrail#InvalidS3PrefixException``."""

    code: str | None = "InvalidS3PrefixException"

    def __init__(self, data: InvalidS3PrefixException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidS3PrefixException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidS3PrefixException":
        return cls(deserialize_aws_json_1_1(data))
