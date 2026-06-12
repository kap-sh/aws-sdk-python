"""Generated from Smithy shape ``com.amazonaws.iot#CertificateValidationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iot.types.error_message2


class CertificateValidationException_(TypedDict):
    message: NotRequired["aws_sdk_iot.types.error_message2.ErrorMessage2"]
    """<p>Additional information about the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CertificateValidationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> CertificateValidationException_:
    out: CertificateValidationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class CertificateValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iot#CertificateValidationException``."""

    code: str | None = "CertificateValidationException"

    def __init__(self, data: CertificateValidationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CertificateValidationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "CertificateValidationException":
        return cls(deserialize_json(data))
