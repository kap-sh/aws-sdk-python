"""Generated from Smithy shape ``com.amazonaws.drs#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_drs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_drs.types.large_bounded_string


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_drs.types.large_bounded_string.LargeBoundedString"]
    code: NotRequired["aws_sdk_drs.types.large_bounded_string.LargeBoundedString"]
    resource_id: NotRequired[
        "aws_sdk_drs.types.large_bounded_string.LargeBoundedString"
    ]
    """<p>The ID of the resource.</p>"""
    resource_type: NotRequired[
        "aws_sdk_drs.types.large_bounded_string.LargeBoundedString"
    ]
    """<p>The type of the resource.</p>"""
    service_code: NotRequired[
        "aws_sdk_drs.types.large_bounded_string.LargeBoundedString"
    ]
    """<p>Service code.</p>"""
    quota_code: NotRequired["aws_sdk_drs.types.large_bounded_string.LargeBoundedString"]
    """<p>Quota code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "code" in value:
        out["code"] = value["code"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_type" in value:
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
    if "code" in data:
        out["code"] = data["code"]
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    if "serviceCode" in data:
        out["service_code"] = data["serviceCode"]
    if "quotaCode" in data:
        out["quota_code"] = data["quotaCode"]
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.drs#ServiceQuotaExceededException``."""

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
