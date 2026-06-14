"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workspaces_web.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.exception_message
    import aws_sdk_workspaces_web.types.quota_code
    import aws_sdk_workspaces_web.types.resource_id
    import aws_sdk_workspaces_web.types.resource_type
    import aws_sdk_workspaces_web.types.service_code


class ServiceQuotaExceededException_(TypedDict):
    message: NotRequired[
        "aws_sdk_workspaces_web.types.exception_message.ExceptionMessage"
    ]
    resource_id: NotRequired["aws_sdk_workspaces_web.types.resource_id.ResourceId"]
    """<p>Identifier of the resource affected.</p>"""
    resource_type: NotRequired[
        "aws_sdk_workspaces_web.types.resource_type.ResourceType"
    ]
    """<p> Type of the resource affected.</p>"""
    service_code: NotRequired["aws_sdk_workspaces_web.types.service_code.ServiceCode"]
    """<p>The originating service.</p>"""
    quota_code: NotRequired["aws_sdk_workspaces_web.types.quota_code.QuotaCode"]
    """<p>The originating quota.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
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
    """Modeled error for Smithy shape ``com.amazonaws.workspacesweb#ServiceQuotaExceededException``."""

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
