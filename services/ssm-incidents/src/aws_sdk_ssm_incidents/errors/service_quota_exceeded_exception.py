"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.exception_message
    import aws_sdk_ssm_incidents.types.resource_type
    import aws_sdk_ssm_incidents.types.service_code


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "aws_sdk_ssm_incidents.types.exception_message.ExceptionMessage"
    resource_identifier: NotRequired["str"]
    """The identifier for the requested resource"""
    resource_type: NotRequired["aws_sdk_ssm_incidents.types.resource_type.ResourceType"]
    """The resource type"""
    service_code: "aws_sdk_ssm_incidents.types.service_code.ServiceCode"
    """Originating service code"""
    quota_code: "str"
    """Originating quota code"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "resource_identifier" in value:
        out["resourceIdentifier"] = value["resource_identifier"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    out["serviceCode"] = value["service_code"]
    out["quotaCode"] = value["quota_code"]
    return out


def deserialize_json(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ServiceQuotaExceededException_.message required")
    if "resourceIdentifier" in data:
        out["resource_identifier"] = data["resourceIdentifier"]
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
    else:
        raise DeserializationError("ServiceQuotaExceededException_.quota_code required")
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssmincidents#ServiceQuotaExceededException``."""

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
