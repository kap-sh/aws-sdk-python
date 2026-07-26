"""Generated from Smithy shape ``com.amazonaws.iot#CertificateStateException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import ServiceError

if TYPE_CHECKING:
    import capo_iot.types.error_message2


class CertificateStateException_(TypedDict, closed=True):
    message: NotRequired["capo_iot.types.error_message2.ErrorMessage2"]
    """<p>The message for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CertificateStateException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> CertificateStateException_:
    out: CertificateStateException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class CertificateStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iot#CertificateStateException``."""

    code: str | None = "CertificateStateException"

    def __init__(self, data: CertificateStateException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CertificateStateException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "CertificateStateException":
        return cls(deserialize_json(data))
