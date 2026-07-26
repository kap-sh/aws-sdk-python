"""Generated from Smithy shape ``com.amazonaws.wickr#RateLimitError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wickr.errors import ServiceError

if TYPE_CHECKING:
    import capo_wickr.types.generic_string


class RateLimitError_(TypedDict, closed=True):
    message: "capo_wickr.types.generic_string.GenericString"
    """<p>A message indicating that the rate limit was exceeded and suggesting when to retry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RateLimitError_) -> dict:
    out: dict = {}
    out["message"] = value.get("message", "Too many requests sent")
    return out


def deserialize_json(data: dict) -> RateLimitError_:
    out: RateLimitError_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        out["message"] = "Too many requests sent"
    return out


class RateLimitError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wickr#RateLimitError``."""

    code: str | None = "RateLimitError"

    def __init__(self, data: RateLimitError_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RateLimitError",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "RateLimitError":
        return cls(deserialize_json(data))
