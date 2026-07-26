"""Generated from Smithy shape ``com.amazonaws.socialmessaging#AccessDeniedByMetaException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_socialmessaging.errors import ServiceError

if TYPE_CHECKING:
    import capo_socialmessaging.types.error_message


class AccessDeniedByMetaException_(TypedDict, closed=True):
    message: NotRequired["capo_socialmessaging.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: AccessDeniedByMetaException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AccessDeniedByMetaException_:
    out: AccessDeniedByMetaException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class AccessDeniedByMetaException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.socialmessaging#AccessDeniedByMetaException``."""

    code: str | None = "AccessDeniedByMetaException"

    def __init__(self, data: AccessDeniedByMetaException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccessDeniedByMetaException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "AccessDeniedByMetaException":
        return cls(deserialize_json(data))
