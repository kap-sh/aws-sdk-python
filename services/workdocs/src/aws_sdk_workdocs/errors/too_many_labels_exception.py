"""Generated from Smithy shape ``com.amazonaws.workdocs#TooManyLabelsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workdocs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.error_message_type


class TooManyLabelsException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_workdocs.types.error_message_type.ErrorMessageType"]


# --- restJson1 ser/de ---
def serialize_json(value: TooManyLabelsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TooManyLabelsException_:
    out: TooManyLabelsException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class TooManyLabelsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workdocs#TooManyLabelsException``."""

    code: str | None = "TooManyLabelsException"

    def __init__(self, data: TooManyLabelsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyLabelsException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "TooManyLabelsException":
        return cls(deserialize_json(data))
