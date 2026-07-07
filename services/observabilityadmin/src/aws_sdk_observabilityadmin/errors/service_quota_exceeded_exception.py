"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ServiceQuotaExceededException``."""

from typing_extensions import NotRequired, TypedDict

from aws_sdk_observabilityadmin.errors import ServiceError


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: NotRequired["str"]
    resource_id: NotRequired["str"]
    """<p> The identifier of the resource which exceeds the service quota. </p>"""
    resource_type: NotRequired["str"]
    """<p> The type of the resource which exceeds the service quota. </p>"""
    service_code: NotRequired["str"]
    """<p> The code for the service of the exceeded quota. </p>"""
    quota_code: NotRequired["str"]
    """<p> The code for the exceeded service quota. </p>"""
    amzn_error_type: NotRequired["str"]
    """<p> The name of the exception. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "service_code" in value:
        out["ServiceCode"] = value["service_code"]
    if "quota_code" in value:
        out["QuotaCode"] = value["quota_code"]
    return out


def deserialize_json(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "ServiceCode" in data:
        out["service_code"] = data["ServiceCode"]
    if "QuotaCode" in data:
        out["quota_code"] = data["QuotaCode"]
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.observabilityadmin#ServiceQuotaExceededException``."""

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
