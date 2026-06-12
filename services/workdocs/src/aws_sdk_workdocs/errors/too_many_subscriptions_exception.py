"""Generated from Smithy shape ``com.amazonaws.workdocs#TooManySubscriptionsException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workdocs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.error_message_type


class TooManySubscriptionsException_(TypedDict):
    message: NotRequired["aws_sdk_workdocs.types.error_message_type.ErrorMessageType"]


# --- restJson1 ser/de ---
def serialize_json(value: TooManySubscriptionsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TooManySubscriptionsException_:
    out: TooManySubscriptionsException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class TooManySubscriptionsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workdocs#TooManySubscriptionsException``."""

    code: str | None = "TooManySubscriptionsException"

    def __init__(self, data: TooManySubscriptionsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManySubscriptionsException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "TooManySubscriptionsException":
        return cls(deserialize_json(data))
