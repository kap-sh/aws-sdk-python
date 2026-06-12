"""Generated from Smithy shape ``com.amazonaws.support#AttachmentSetExpired``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_support.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_support.types.error_message


class AttachmentSetExpired_(TypedDict):
    message: NotRequired["aws_sdk_support.types.error_message.ErrorMessage"]
    """<p>The expiration time of the attachment set has passed. The set expires one hour after it is created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachmentSetExpired_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AttachmentSetExpired_:
    out: AttachmentSetExpired_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class AttachmentSetExpired(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.support#AttachmentSetExpired``."""

    code: str | None = "AttachmentSetExpired"

    def __init__(self, data: AttachmentSetExpired_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AttachmentSetExpired",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "AttachmentSetExpired":
        return cls(deserialize_aws_json_1_1(data))
