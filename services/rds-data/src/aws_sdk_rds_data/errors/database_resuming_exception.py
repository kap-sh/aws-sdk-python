"""Generated from Smithy shape ``com.amazonaws.rdsdata#DatabaseResumingException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds_data.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.error_message


class DatabaseResumingException_(TypedDict):
    message: NotRequired["aws_sdk_rds_data.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: DatabaseResumingException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DatabaseResumingException_:
    out: DatabaseResumingException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class DatabaseResumingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rdsdata#DatabaseResumingException``."""

    code: str | None = "DatabaseResumingException"

    def __init__(self, data: DatabaseResumingException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DatabaseResumingException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "DatabaseResumingException":
        return cls(deserialize_json(data))
