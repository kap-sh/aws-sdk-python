"""Generated from Smithy shape ``com.amazonaws.guardduty#AccessDeniedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_guardduty.errors import ServiceError

if TYPE_CHECKING:
    import capo_guardduty.types.string


class AccessDeniedException_(TypedDict, closed=True):
    message: NotRequired["capo_guardduty.types.string.String"]
    """<p>The error message.</p>"""
    type: NotRequired["capo_guardduty.types.string.String"]
    """<p>The error type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessDeniedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "type" in data:
        out["type"] = data["type"]
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.guardduty#AccessDeniedException``."""

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
