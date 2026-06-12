"""Generated from Smithy shape ``com.amazonaws.rdsdata#UnsupportedResultException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds_data.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.error_message


class UnsupportedResultException_(TypedDict):
    message: NotRequired["aws_sdk_rds_data.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: UnsupportedResultException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnsupportedResultException_:
    out: UnsupportedResultException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class UnsupportedResultException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rdsdata#UnsupportedResultException``."""

    code: str | None = "UnsupportedResultException"

    def __init__(self, data: UnsupportedResultException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedResultException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "UnsupportedResultException":
        return cls(deserialize_json(data))
