"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_marketplace_agreement.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.bounded_string
    import aws_sdk_marketplace_agreement.types.exception_message
    import aws_sdk_marketplace_agreement.types.request_id
    import aws_sdk_marketplace_agreement.types.resource_id


class ServiceQuotaExceededException_(TypedDict, closed=True):
    request_id: NotRequired["aws_sdk_marketplace_agreement.types.request_id.RequestId"]
    """<p>The unique identifier for the error.</p>"""
    message: NotRequired[
        "aws_sdk_marketplace_agreement.types.exception_message.ExceptionMessage"
    ]
    """<p>Description of the error.</p>"""
    quota_code: NotRequired[
        "aws_sdk_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>The code of the quota that was exceeded.</p>"""
    service_code: NotRequired[
        "aws_sdk_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>The code of the service whose quota was exceeded.</p>"""
    resource_type: NotRequired[
        "aws_sdk_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>The type of the resource that exceeded the quota.</p>"""
    resource_id: NotRequired[
        "aws_sdk_marketplace_agreement.types.resource_id.ResourceId"
    ]
    """<p>The unique identifier of the resource that exceeded the quota.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "message" in value:
        out["message"] = value["message"]
    if "quota_code" in value:
        out["quotaCode"] = value["quota_code"]
    if "service_code" in value:
        out["serviceCode"] = value["service_code"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "message" in data:
        out["message"] = data["message"]
    if "quotaCode" in data:
        out["quota_code"] = data["quotaCode"]
    if "serviceCode" in data:
        out["service_code"] = data["serviceCode"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.marketplaceagreement#ServiceQuotaExceededException``."""

    code: str | None = "ServiceQuotaExceededException"

    def __init__(self, data: ServiceQuotaExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceQuotaExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "ServiceQuotaExceededException":
        return cls(deserialize_aws_json_1_0(data))
