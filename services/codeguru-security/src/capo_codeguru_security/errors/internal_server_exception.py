"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#InternalServerException``."""

from typing_extensions import NotRequired, TypedDict

from capo_codeguru_security.errors import ServiceError


class InternalServerException_(TypedDict, closed=True):
    error: NotRequired["str"]
    """<p>The internal error encountered by the server.</p>"""
    message: NotRequired["str"]
    """<p>Description of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerException_) -> dict:
    out: dict = {}
    if "error" in value:
        out["error"] = value["error"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if "error" in data:
        out["error"] = data["error"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codegurusecurity#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(self, data: InternalServerException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=True,
            code="InternalServerException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InternalServerException":
        return cls(deserialize_json(data))
