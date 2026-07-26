"""Generated from Smithy shape ``com.amazonaws.taxsettings#AttachmentUploadException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_taxsettings.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_taxsettings.types.error_message


class AttachmentUploadException_(TypedDict, closed=True):
    message: "capo_taxsettings.types.error_message.ErrorMessage"


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentUploadException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AttachmentUploadException_:
    out: AttachmentUploadException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("AttachmentUploadException_.message required")
    return out


class AttachmentUploadException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.taxsettings#AttachmentUploadException``."""

    code: str | None = "AttachmentUploadException"

    def __init__(self, data: AttachmentUploadException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AttachmentUploadException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "AttachmentUploadException":
        return cls(deserialize_json(data))
