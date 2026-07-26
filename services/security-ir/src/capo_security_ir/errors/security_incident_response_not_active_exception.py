"""Generated from Smithy shape ``com.amazonaws.securityir#SecurityIncidentResponseNotActiveException``."""

from typing_extensions import TypedDict

from capo_security_ir.errors import DeserializationError, ServiceError


class SecurityIncidentResponseNotActiveException_(TypedDict, closed=True):
    message: "str"
    """<p>The exception message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityIncidentResponseNotActiveException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> SecurityIncidentResponseNotActiveException_:
    out: SecurityIncidentResponseNotActiveException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError(
            "SecurityIncidentResponseNotActiveException_.message required"
        )
    return out


class SecurityIncidentResponseNotActiveException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.securityir#SecurityIncidentResponseNotActiveException``."""

    code: str | None = "SecurityIncidentResponseNotActiveException"

    def __init__(self, data: SecurityIncidentResponseNotActiveException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SecurityIncidentResponseNotActiveException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "SecurityIncidentResponseNotActiveException":
        return cls(deserialize_json(data))
