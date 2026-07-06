"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ServiceQuotaExceededException``."""

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route53globalresolver.errors import DeserializationError, ServiceError


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "str"
    resource_id: NotRequired["str"]
    """<p>The unique ID of the resource referenced in the failed request.</p>"""
    resource_type: "str"
    """<p>The resource type of the resource referenced in the failed request.</p>"""
    service_code: NotRequired["str"]
    """<p>The code for the Amazon Web Services service that owns the quota.</p>"""
    quota_code: NotRequired["str"]
    """<p>The quota code recognized by the Amazon Web Services Service Quotas service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    out["resourceType"] = value["resource_type"]
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
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError(
            "ServiceQuotaExceededException_.resource_type required"
        )
    if "serviceCode" in data:
        out["service_code"] = data["serviceCode"]
    if "quotaCode" in data:
        out["quota_code"] = data["quotaCode"]
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53globalresolver#ServiceQuotaExceededException``."""

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
