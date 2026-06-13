"""Generated from Smithy shape ``com.amazonaws.taxsettings#ConflictException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_taxsettings.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.error_code
    import aws_sdk_taxsettings.types.error_message


class ConflictException_(TypedDict):
    message: "aws_sdk_taxsettings.types.error_message.ErrorMessage"
    error_code: "aws_sdk_taxsettings.types.error_code.ErrorCode"
    """<p>409</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["errorCode"] = value["error_code"]
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ConflictException_.message required")
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    else:
        raise DeserializationError("ConflictException_.error_code required")
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.taxsettings#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(self, data: ConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ConflictException":
        return cls(deserialize_json(data))
