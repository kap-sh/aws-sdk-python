"""Generated from Smithy shape ``com.amazonaws.qbusiness#LicenseNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qbusiness.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.error_message


class LicenseNotFoundException_(TypedDict, closed=True):
    message: "aws_sdk_qbusiness.types.error_message.ErrorMessage"


# --- restJson1 ser/de ---
def serialize_json(value: LicenseNotFoundException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> LicenseNotFoundException_:
    out: LicenseNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("LicenseNotFoundException_.message required")
    return out


class LicenseNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.qbusiness#LicenseNotFoundException``."""

    code: str | None = "LicenseNotFoundException"

    def __init__(self, data: LicenseNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LicenseNotFoundException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "LicenseNotFoundException":
        return cls(deserialize_json(data))
