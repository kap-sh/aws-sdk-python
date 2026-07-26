"""Generated from Smithy shape ``com.amazonaws.appsync#ApiKeyLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appsync.errors import ServiceError

if TYPE_CHECKING:
    import capo_appsync.types.string


class ApiKeyLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_appsync.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ApiKeyLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ApiKeyLimitExceededException_:
    out: ApiKeyLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ApiKeyLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.appsync#ApiKeyLimitExceededException``."""

    code: str | None = "ApiKeyLimitExceededException"

    def __init__(self, data: ApiKeyLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ApiKeyLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ApiKeyLimitExceededException":
        return cls(deserialize_json(data))
