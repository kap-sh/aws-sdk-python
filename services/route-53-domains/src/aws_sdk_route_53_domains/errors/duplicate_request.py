"""Generated from Smithy shape ``com.amazonaws.route53domains#DuplicateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route_53_domains.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.error_message
    import aws_sdk_route_53_domains.types.request_id


class DuplicateRequest_(TypedDict, closed=True):
    request_id: NotRequired["aws_sdk_route_53_domains.types.request_id.RequestId"]
    """<p>ID of the request operation.</p>"""
    message: NotRequired["aws_sdk_route_53_domains.types.error_message.ErrorMessage"]
    """<p>The request is already in progress for the domain.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DuplicateRequest_) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DuplicateRequest_:
    out: DuplicateRequest_ = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class DuplicateRequest(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53domains#DuplicateRequest``."""

    code: str | None = "DuplicateRequest"

    def __init__(self, data: DuplicateRequest_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DuplicateRequest",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "DuplicateRequest":
        return cls(deserialize_aws_json_1_1(data))
