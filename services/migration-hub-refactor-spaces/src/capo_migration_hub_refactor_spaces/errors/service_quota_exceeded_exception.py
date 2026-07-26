"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_migration_hub_refactor_spaces.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.string


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "capo_migration_hub_refactor_spaces.types.string.String"
    resource_id: "capo_migration_hub_refactor_spaces.types.string.String"
    """<p>The ID of the resource. </p>"""
    resource_type: "capo_migration_hub_refactor_spaces.types.string.String"
    """<p>The type of resource. </p>"""
    quota_code: NotRequired["capo_migration_hub_refactor_spaces.types.string.String"]
    """<p>Service quota requirement to identify originating quota. Reached throttling quota exception. </p>"""
    service_code: "capo_migration_hub_refactor_spaces.types.string.String"
    """<p>Service quota requirement to identify originating service. Reached throttling quota exception service code. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    out["ResourceId"] = value["resource_id"]
    out["ResourceType"] = value["resource_type"]
    if "quota_code" in value:
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
    else:
        raise DeserializationError(
            "ServiceQuotaExceededException_.resource_id required"
        )
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    else:
        raise DeserializationError(
            "ServiceQuotaExceededException_.resource_type required"
        )
    if "QuotaCode" in data:
        out["quota_code"] = data["QuotaCode"]
    if "ServiceCode" in data:
        out["service_code"] = data["ServiceCode"]
    else:
        raise DeserializationError(
            "ServiceQuotaExceededException_.service_code required"
        )
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.migrationhubrefactorspaces#ServiceQuotaExceededException``."""

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
