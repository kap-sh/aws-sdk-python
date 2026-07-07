"""Generated from Smithy shape ``com.amazonaws.rdsdata#SecretsErrorException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds_data.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.error_message


class SecretsErrorException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_rds_data.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: SecretsErrorException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> SecretsErrorException_:
    out: SecretsErrorException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class SecretsErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rdsdata#SecretsErrorException``."""

    code: str | None = "SecretsErrorException"

    def __init__(self, data: SecretsErrorException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SecretsErrorException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "SecretsErrorException":
        return cls(deserialize_json(data))
