"""Generated from Smithy shape ``com.amazonaws.taxsettings#CaseCreationLimitExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_taxsettings.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.error_message


class CaseCreationLimitExceededException_(TypedDict):
    message: "aws_sdk_taxsettings.types.error_message.ErrorMessage"


# --- restJson1 ser/de ---
def serialize_json(value: CaseCreationLimitExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> CaseCreationLimitExceededException_:
    out: CaseCreationLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError(
            "CaseCreationLimitExceededException_.message required"
        )
    return out


class CaseCreationLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.taxsettings#CaseCreationLimitExceededException``."""

    code: str | None = "CaseCreationLimitExceededException"

    def __init__(self, data: CaseCreationLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CaseCreationLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "CaseCreationLimitExceededException":
        return cls(deserialize_json(data))
