"""Generated from Smithy shape ``com.amazonaws.support#DescribeAttachmentLimitExceeded``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_support.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_support.types.error_message


class DescribeAttachmentLimitExceeded_(TypedDict):
    message: NotRequired["aws_sdk_support.types.error_message.ErrorMessage"]
    """<p>The limit for the number of <a>DescribeAttachment</a> requests in a short period of time has been exceeded.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAttachmentLimitExceeded_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAttachmentLimitExceeded_:
    out: DescribeAttachmentLimitExceeded_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class DescribeAttachmentLimitExceeded(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.support#DescribeAttachmentLimitExceeded``."""

    code: str | None = "DescribeAttachmentLimitExceeded"

    def __init__(self, data: DescribeAttachmentLimitExceeded_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DescribeAttachmentLimitExceeded",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "DescribeAttachmentLimitExceeded":
        return cls(deserialize_aws_json_1_1(data))
