"""Generated from Smithy shape ``com.amazonaws.cloudtrail#InsufficientS3BucketPolicyException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudtrail.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.error_message


class InsufficientS3BucketPolicyException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_cloudtrail.types.error_message.ErrorMessage"]
    """<p>Brief description of the exception returned by the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InsufficientS3BucketPolicyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InsufficientS3BucketPolicyException_:
    out: InsufficientS3BucketPolicyException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InsufficientS3BucketPolicyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudtrail#InsufficientS3BucketPolicyException``."""

    code: str | None = "InsufficientS3BucketPolicyException"

    def __init__(self, data: InsufficientS3BucketPolicyException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InsufficientS3BucketPolicyException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InsufficientS3BucketPolicyException":
        return cls(deserialize_aws_json_1_1(data))
