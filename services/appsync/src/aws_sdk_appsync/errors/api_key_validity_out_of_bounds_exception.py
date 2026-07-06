"""Generated from Smithy shape ``com.amazonaws.appsync#ApiKeyValidityOutOfBoundsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appsync.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_appsync.types.string


class ApiKeyValidityOutOfBoundsException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_appsync.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ApiKeyValidityOutOfBoundsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ApiKeyValidityOutOfBoundsException_:
    out: ApiKeyValidityOutOfBoundsException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ApiKeyValidityOutOfBoundsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.appsync#ApiKeyValidityOutOfBoundsException``."""

    code: str | None = "ApiKeyValidityOutOfBoundsException"

    def __init__(self, data: ApiKeyValidityOutOfBoundsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ApiKeyValidityOutOfBoundsException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ApiKeyValidityOutOfBoundsException":
        return cls(deserialize_json(data))
