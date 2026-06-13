"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ThrottlingException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_marketplace_agreement.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.exception_message
    import aws_sdk_marketplace_agreement.types.request_id


class ThrottlingException_(TypedDict):
    request_id: NotRequired["aws_sdk_marketplace_agreement.types.request_id.RequestId"]
    """<p>The unique identifier for the error.</p>"""
    message: NotRequired[
        "aws_sdk_marketplace_agreement.types.exception_message.ExceptionMessage"
    ]
    """<p>Description of the error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ThrottlingException_) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.marketplaceagreement#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(self, data: ThrottlingException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottlingException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "ThrottlingException":
        return cls(deserialize_aws_json_1_0(data))
