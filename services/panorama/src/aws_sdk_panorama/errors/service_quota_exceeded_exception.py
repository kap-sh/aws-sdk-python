"""Generated from Smithy shape ``com.amazonaws.panorama#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_panorama.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.string


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "aws_sdk_panorama.types.string.String"
    resource_id: NotRequired["aws_sdk_panorama.types.string.String"]
    """<p>The target resource's ID.</p>"""
    resource_type: NotRequired["aws_sdk_panorama.types.string.String"]
    """<p>The target resource's type.</p>"""
    quota_code: "aws_sdk_panorama.types.string.String"
    """<p>The name of the limit.</p>"""
    service_code: "aws_sdk_panorama.types.string.String"
    """<p>The name of the service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    out["QuotaCode"] = value["quota_code"]
    out["ServiceCode"] = value["service_code"]
    return out


def deserialize_json(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ServiceQuotaExceededException_.message required")
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "QuotaCode" in data:
        out["quota_code"] = data["QuotaCode"]
    else:
        raise DeserializationError("ServiceQuotaExceededException_.quota_code required")
    if "ServiceCode" in data:
        out["service_code"] = data["ServiceCode"]
    else:
        raise DeserializationError(
            "ServiceQuotaExceededException_.service_code required"
        )
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.panorama#ServiceQuotaExceededException``."""

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
