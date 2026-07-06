"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#ServiceQuotaExceededException``."""

from typing_extensions import NotRequired, TypedDict

from aws_sdk_opensearchserverless.errors import DeserializationError, ServiceError


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "str"
    """Description of the error."""
    resource_id: NotRequired["str"]
    """Identifier of the resource affected."""
    resource_type: NotRequired["str"]
    """Type of the resource affected."""
    service_code: "str"
    """Service Quotas requirement to identify originating service."""
    quota_code: NotRequired["str"]
    """Service Quotas requirement to identify originating quota."""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    out["serviceCode"] = value["service_code"]
    if "quota_code" in value:
        out["quotaCode"] = value["quota_code"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ServiceQuotaExceededException_.message required")
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    if "serviceCode" in data:
        out["service_code"] = data["serviceCode"]
    else:
        raise DeserializationError(
            "ServiceQuotaExceededException_.service_code required"
        )
    if "quotaCode" in data:
        out["quota_code"] = data["quotaCode"]
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.opensearchserverless#ServiceQuotaExceededException``."""

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
