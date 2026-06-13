"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ServiceQuotaExceededException``."""

from typing import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError, ServiceError


class ServiceQuotaExceededException_(TypedDict):
    message: "str"
    quota_name: "str"
    """<p>The name of the quota.</p>"""
    quota_value: "float"
    """<p>The value of the quota.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["quotaName"] = value["quota_name"]
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
    else:
        raise DeserializationError("ServiceQuotaExceededException_.quota_name required")
    if "quotaValue" in data:
        out["quota_value"] = data["quotaValue"]
    else:
        raise DeserializationError(
            "ServiceQuotaExceededException_.quota_value required"
        )
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cleanrooms#ServiceQuotaExceededException``."""

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
