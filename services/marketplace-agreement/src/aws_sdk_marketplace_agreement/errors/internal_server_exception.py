"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#InternalServerException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_marketplace_agreement.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.exception_message
    import aws_sdk_marketplace_agreement.types.request_id


class InternalServerException_(TypedDict, closed=True):
    request_id: NotRequired["aws_sdk_marketplace_agreement.types.request_id.RequestId"]
    """<p>The unique identifier for the error.</p>"""
    message: NotRequired[
        "aws_sdk_marketplace_agreement.types.exception_message.ExceptionMessage"
    ]
    """<p>Description of the error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InternalServerException_) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.marketplaceagreement#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(self, data: InternalServerException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "InternalServerException":
        return cls(deserialize_aws_json_1_0(data))
