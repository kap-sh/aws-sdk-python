"""Generated from Smithy shape ``com.amazonaws.wickr#BadRequestError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wickr.errors import ServiceError

if TYPE_CHECKING:
    import capo_wickr.types.generic_string


class BadRequestError_(TypedDict, closed=True):
    message: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>A detailed message explaining what was wrong with the request and how to correct it.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BadRequestError_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BadRequestError_:
    out: BadRequestError_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class BadRequestError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wickr#BadRequestError``."""

    code: str | None = "BadRequestError"

    def __init__(self, data: BadRequestError_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BadRequestError",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "BadRequestError":
        return cls(deserialize_json(data))
