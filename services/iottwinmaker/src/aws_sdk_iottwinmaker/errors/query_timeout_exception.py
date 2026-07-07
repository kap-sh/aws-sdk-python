"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#QueryTimeoutException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iottwinmaker.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.error_message


class QueryTimeoutException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_iottwinmaker.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: QueryTimeoutException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> QueryTimeoutException_:
    out: QueryTimeoutException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class QueryTimeoutException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iottwinmaker#QueryTimeoutException``."""

    code: str | None = "QueryTimeoutException"

    def __init__(self, data: QueryTimeoutException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=True,
            code="QueryTimeoutException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "QueryTimeoutException":
        return cls(deserialize_json(data))
