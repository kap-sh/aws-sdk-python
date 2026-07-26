"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ServiceQuotaExceededException``."""

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError, ServiceError


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "str"
    quota_name: NotRequired["str"]
    """The name of the service quota limit that was exceeded"""
    quota_value: NotRequired["float"]
    """The current limit on the service quota that was exceeded"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "quota_name" in value:
        out["quotaName"] = value["quota_name"]
    if "quota_value" in value:
        out["quotaValue"] = value["quota_value"]
    return out


def deserialize_json(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ServiceQuotaExceededException_.message required")
    if "quotaName" in data:
        out["quota_name"] = data["quotaName"]
    if "quotaValue" in data:
        out["quota_value"] = data["quotaValue"]
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cleanroomsml#ServiceQuotaExceededException``."""

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
