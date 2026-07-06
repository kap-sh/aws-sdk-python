"""Generated from Smithy shape ``com.amazonaws.greengrassv2#RequestAlreadyInProgressException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_greengrassv2.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.string


class RequestAlreadyInProgressException_(TypedDict, closed=True):
    message: "aws_sdk_greengrassv2.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: RequestAlreadyInProgressException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RequestAlreadyInProgressException_:
    out: RequestAlreadyInProgressException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError(
            "RequestAlreadyInProgressException_.message required"
        )
    return out


class RequestAlreadyInProgressException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.greengrassv2#RequestAlreadyInProgressException``."""

    code: str | None = "RequestAlreadyInProgressException"

    def __init__(self, data: RequestAlreadyInProgressException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RequestAlreadyInProgressException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "RequestAlreadyInProgressException":
        return cls(deserialize_json(data))
