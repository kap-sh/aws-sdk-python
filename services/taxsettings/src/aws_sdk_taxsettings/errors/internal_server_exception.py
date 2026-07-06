"""Generated from Smithy shape ``com.amazonaws.taxsettings#InternalServerException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_taxsettings.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.error_code
    import aws_sdk_taxsettings.types.error_message


class InternalServerException_(TypedDict, closed=True):
    message: "aws_sdk_taxsettings.types.error_message.ErrorMessage"
    error_code: "aws_sdk_taxsettings.types.error_code.ErrorCode"
    """<p>500</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["errorCode"] = value["error_code"]
    return out


def deserialize_json(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InternalServerException_.message required")
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    else:
        raise DeserializationError("InternalServerException_.error_code required")
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.taxsettings#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(self, data: InternalServerException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InternalServerException":
        return cls(deserialize_json(data))
