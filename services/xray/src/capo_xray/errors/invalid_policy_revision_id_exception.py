"""Generated from Smithy shape ``com.amazonaws.xray#InvalidPolicyRevisionIdException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_xray.errors import ServiceError

if TYPE_CHECKING:
    import capo_xray.types.error_message


class InvalidPolicyRevisionIdException_(TypedDict, closed=True):
    message: NotRequired["capo_xray.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidPolicyRevisionIdException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidPolicyRevisionIdException_:
    out: InvalidPolicyRevisionIdException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidPolicyRevisionIdException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.xray#InvalidPolicyRevisionIdException``."""

    code: str | None = "InvalidPolicyRevisionIdException"

    def __init__(self, data: InvalidPolicyRevisionIdException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidPolicyRevisionIdException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidPolicyRevisionIdException":
        return cls(deserialize_json(data))
