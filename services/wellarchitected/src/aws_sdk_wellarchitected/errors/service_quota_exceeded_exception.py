"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wellarchitected.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.exception_message
    import aws_sdk_wellarchitected.types.exception_resource_id
    import aws_sdk_wellarchitected.types.exception_resource_type
    import aws_sdk_wellarchitected.types.quota_code
    import aws_sdk_wellarchitected.types.service_code


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_wellarchitected.types.exception_message.ExceptionMessage"
    ]
    resource_id: NotRequired[
        "aws_sdk_wellarchitected.types.exception_resource_id.ExceptionResourceId"
    ]
    resource_type: NotRequired[
        "aws_sdk_wellarchitected.types.exception_resource_type.ExceptionResourceType"
    ]
    quota_code: NotRequired["aws_sdk_wellarchitected.types.quota_code.QuotaCode"]
    service_code: NotRequired["aws_sdk_wellarchitected.types.service_code.ServiceCode"]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "quota_code" in value:
        out["QuotaCode"] = value["quota_code"]
    if "service_code" in value:
        out["ServiceCode"] = value["service_code"]
    return out


def deserialize_json(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "QuotaCode" in data:
        out["quota_code"] = data["QuotaCode"]
    if "ServiceCode" in data:
        out["service_code"] = data["ServiceCode"]
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wellarchitected#ServiceQuotaExceededException``."""

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
