"""Generated from Smithy shape ``com.amazonaws.novaact#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_nova_act.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.non_blank_string


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "aws_sdk_nova_act.types.non_blank_string.NonBlankString"
    """<p>The request would exceed one or more service quotas for your account.</p>"""
    resource_id: "aws_sdk_nova_act.types.non_blank_string.NonBlankString"
    """<p>The identifier of the resource that exceeded the quota.</p>"""
    resource_type: "aws_sdk_nova_act.types.non_blank_string.NonBlankString"
    """<p>The type of resource that exceeded the quota.</p>"""
    service_code: "aws_sdk_nova_act.types.non_blank_string.NonBlankString"
    """<p>The service code for the quota that was exceeded.</p>"""
    quota_code: "aws_sdk_nova_act.types.non_blank_string.NonBlankString"
    """<p>The code for the specific quota that was exceeded.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resourceId"] = value["resource_id"]
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
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError(
            "ServiceQuotaExceededException_.resource_id required"
        )
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError(
            "ServiceQuotaExceededException_.resource_type required"
        )
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
    """Modeled error for Smithy shape ``com.amazonaws.novaact#ServiceQuotaExceededException``."""

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
