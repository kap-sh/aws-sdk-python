"""Generated from Smithy shape ``com.amazonaws.oam#InternalServiceFault``."""

from typing_extensions import NotRequired, TypedDict

from capo_oam.errors import ServiceError


class InternalServiceFault_(TypedDict, closed=True):
    message: NotRequired["str"]
    amzn_error_type: NotRequired["str"]
    """<p>The name of the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalServiceFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServiceFault_:
    out: InternalServiceFault_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InternalServiceFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.oam#InternalServiceFault``."""

    code: str | None = "InternalServiceFault"

    def __init__(self, data: InternalServiceFault_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServiceFault",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InternalServiceFault":
        return cls(deserialize_json(data))
