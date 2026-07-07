"""Generated from Smithy shape ``com.amazonaws.xray#RuleLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_xray.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_xray.types.error_message


class RuleLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_xray.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: RuleLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RuleLimitExceededException_:
    out: RuleLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class RuleLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.xray#RuleLimitExceededException``."""

    code: str | None = "RuleLimitExceededException"

    def __init__(self, data: RuleLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RuleLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "RuleLimitExceededException":
        return cls(deserialize_json(data))
