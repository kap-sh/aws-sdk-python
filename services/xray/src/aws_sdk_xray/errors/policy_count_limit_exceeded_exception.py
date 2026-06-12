"""Generated from Smithy shape ``com.amazonaws.xray#PolicyCountLimitExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_xray.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_xray.types.error_message


class PolicyCountLimitExceededException_(TypedDict):
    message: NotRequired["aws_sdk_xray.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyCountLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> PolicyCountLimitExceededException_:
    out: PolicyCountLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class PolicyCountLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.xray#PolicyCountLimitExceededException``."""

    code: str | None = "PolicyCountLimitExceededException"

    def __init__(self, data: PolicyCountLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PolicyCountLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "PolicyCountLimitExceededException":
        return cls(deserialize_json(data))
