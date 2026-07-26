"""Generated from Smithy shape ``com.amazonaws.groundstation#ServiceQuotaExceededException``."""

from typing_extensions import NotRequired, TypedDict

from capo_groundstation.errors import ServiceError


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: NotRequired["str"]
    parameter_name: NotRequired["str"]
    """<p>Parameter name that caused the exception</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "parameter_name" in value:
        out["parameterName"] = value["parameter_name"]
    return out


def deserialize_json(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "parameterName" in data:
        out["parameter_name"] = data["parameterName"]
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.groundstation#ServiceQuotaExceededException``."""

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
