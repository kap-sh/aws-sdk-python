"""Generated from Smithy shape ``com.amazonaws.support#AttachmentLimitExceeded``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_support.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_support.types.error_message


class AttachmentLimitExceeded_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_support.types.error_message.ErrorMessage"]
    """<p>The limit for the number of attachment sets created in a short period of time has been exceeded.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachmentLimitExceeded_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AttachmentLimitExceeded_:
    out: AttachmentLimitExceeded_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class AttachmentLimitExceeded(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.support#AttachmentLimitExceeded``."""

    code: str | None = "AttachmentLimitExceeded"

    def __init__(self, data: AttachmentLimitExceeded_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AttachmentLimitExceeded",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "AttachmentLimitExceeded":
        return cls(deserialize_aws_json_1_1(data))
