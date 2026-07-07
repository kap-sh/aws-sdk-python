"""Generated from Smithy shape ``com.amazonaws.rdsdata#InvalidSecretException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds_data.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.error_message


class InvalidSecretException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_rds_data.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidSecretException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidSecretException_:
    out: InvalidSecretException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidSecretException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rdsdata#InvalidSecretException``."""

    code: str | None = "InvalidSecretException"

    def __init__(self, data: InvalidSecretException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidSecretException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidSecretException":
        return cls(deserialize_json(data))
