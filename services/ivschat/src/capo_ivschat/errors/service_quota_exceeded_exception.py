"""Generated from Smithy shape ``com.amazonaws.ivschat#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ivschat.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_ivschat.types.error_message
    import capo_ivschat.types.limit
    import capo_ivschat.types.resource_id
    import capo_ivschat.types.resource_type


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "capo_ivschat.types.error_message.ErrorMessage"
    resource_id: "capo_ivschat.types.resource_id.ResourceId"
    """<p/>"""
    resource_type: "capo_ivschat.types.resource_type.ResourceType"
    """<p/>"""
    limit: "capo_ivschat.types.limit.Limit"
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resourceId"] = value["resource_id"]
    out["resourceType"] = value["resource_type"]
    out["limit"] = value.get("limit", 0)
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
    if "limit" in data:
        out["limit"] = data["limit"]
    else:
        out["limit"] = 0
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ivschat#ServiceQuotaExceededException``."""

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
