"""Generated from Smithy shape ``com.amazonaws.networkmanager#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_networkmanager.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.server_side_string


class ServiceQuotaExceededException_(TypedDict):
    message: "aws_sdk_networkmanager.types.server_side_string.ServerSideString"
    """<p>The error message.</p>"""
    resource_id: NotRequired[
        "aws_sdk_networkmanager.types.server_side_string.ServerSideString"
    ]
    """<p>The ID of the resource.</p>"""
    resource_type: NotRequired[
        "aws_sdk_networkmanager.types.server_side_string.ServerSideString"
    ]
    """<p>The resource type.</p>"""
    limit_code: "aws_sdk_networkmanager.types.server_side_string.ServerSideString"
    """<p>The limit code.</p>"""
    service_code: "aws_sdk_networkmanager.types.server_side_string.ServerSideString"
    """<p>The service code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    out["LimitCode"] = value["limit_code"]
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
    if "LimitCode" in data:
        out["limit_code"] = data["LimitCode"]
    else:
        raise DeserializationError("ServiceQuotaExceededException_.limit_code required")
    if "ServiceCode" in data:
        out["service_code"] = data["ServiceCode"]
    else:
        raise DeserializationError(
            "ServiceQuotaExceededException_.service_code required"
        )
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.networkmanager#ServiceQuotaExceededException``."""

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
