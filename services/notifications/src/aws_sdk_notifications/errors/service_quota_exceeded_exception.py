"""Generated from Smithy shape ``com.amazonaws.notifications#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_notifications.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.error_message
    import aws_sdk_notifications.types.quota_code
    import aws_sdk_notifications.types.resource_id
    import aws_sdk_notifications.types.resource_type
    import aws_sdk_notifications.types.service_code


class ServiceQuotaExceededException_(TypedDict):
    message: "aws_sdk_notifications.types.error_message.ErrorMessage"
    resource_type: "aws_sdk_notifications.types.resource_type.ResourceType"
    """<p>The type of the resource that exceeds the service quota.</p>"""
    resource_id: NotRequired["aws_sdk_notifications.types.resource_id.ResourceId"]
    """<p>The ID of the resource that exceeds the service quota.</p>"""
    service_code: NotRequired["aws_sdk_notifications.types.service_code.ServiceCode"]
    r"""<p>The code for the service quota exceeded in <a href=\"https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html\">Service Quotas</a>.</p>"""
    quota_code: NotRequired["aws_sdk_notifications.types.quota_code.QuotaCode"]
    r"""<p>The code for the service quota in <a href=\"https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html\">Service Quotas</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resourceType"] = value["resource_type"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "service_code" in value:
        out["serviceCode"] = value["service_code"]
    if "quota_code" in value:
        out["quotaCode"] = value["quota_code"]
    return out


def deserialize_json(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ServiceQuotaExceededException_.message required")
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError(
            "ServiceQuotaExceededException_.resource_type required"
        )
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "serviceCode" in data:
        out["service_code"] = data["serviceCode"]
    if "quotaCode" in data:
        out["quota_code"] = data["quotaCode"]
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.notifications#ServiceQuotaExceededException``."""

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
    def from_json(cls, data: dict) -> "ServiceQuotaExceededException":
        return cls(deserialize_json(data))
