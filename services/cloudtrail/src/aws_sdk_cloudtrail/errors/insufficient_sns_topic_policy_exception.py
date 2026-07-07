"""Generated from Smithy shape ``com.amazonaws.cloudtrail#InsufficientSnsTopicPolicyException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudtrail.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.error_message


class InsufficientSnsTopicPolicyException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_cloudtrail.types.error_message.ErrorMessage"]
    """<p>Brief description of the exception returned by the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InsufficientSnsTopicPolicyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InsufficientSnsTopicPolicyException_:
    out: InsufficientSnsTopicPolicyException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InsufficientSnsTopicPolicyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudtrail#InsufficientSnsTopicPolicyException``."""

    code: str | None = "InsufficientSnsTopicPolicyException"

    def __init__(self, data: InsufficientSnsTopicPolicyException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InsufficientSnsTopicPolicyException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InsufficientSnsTopicPolicyException":
        return cls(deserialize_aws_json_1_1(data))
