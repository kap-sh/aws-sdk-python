"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AccessDeniedException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.access_denied_exception_reason


class AccessDeniedException_(TypedDict):
    message: NotRequired["str"]
    reason: NotRequired[
        "aws_sdk_cleanrooms.types.access_denied_exception_reason.AccessDeniedExceptionReason"
    ]
    """<p>A reason code for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessDeniedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "reason" in data:
        out["reason"] = data["reason"]
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cleanrooms#AccessDeniedException``."""

    code: str | None = "AccessDeniedException"

    def __init__(self, data: AccessDeniedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccessDeniedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "AccessDeniedException":
        return cls(deserialize_json(data))
