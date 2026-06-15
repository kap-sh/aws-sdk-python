"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_greengrassv2.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.string


class ServiceQuotaExceededException_(TypedDict):
    message: "aws_sdk_greengrassv2.types.string.String"
    resource_id: NotRequired["aws_sdk_greengrassv2.types.string.String"]
    """<p>The ID of the resource that exceeds the service quota.</p>"""
    resource_type: NotRequired["aws_sdk_greengrassv2.types.string.String"]
    """<p>The type of the resource that exceeds the service quota.</p>"""
    quota_code: "aws_sdk_greengrassv2.types.string.String"
    r"""<p>The code for the quota in <a href=\"https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html\">Service Quotas</a>.</p>"""
    service_code: "aws_sdk_greengrassv2.types.string.String"
    r"""<p>The code for the service in <a href=\"https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html\">Service Quotas</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    out["quotaCode"] = value["quota_code"]
    out["serviceCode"] = value["service_code"]
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
    if "quotaCode" in data:
        out["quota_code"] = data["quotaCode"]
    else:
        raise DeserializationError("ServiceQuotaExceededException_.quota_code required")
    if "serviceCode" in data:
        out["service_code"] = data["serviceCode"]
    else:
        raise DeserializationError(
            "ServiceQuotaExceededException_.service_code required"
        )
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.greengrassv2#ServiceQuotaExceededException``."""

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
