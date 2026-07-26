"""Generated from Smithy shape ``com.amazonaws.iot#IndexNotReadyException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import ServiceError

if TYPE_CHECKING:
    import capo_iot.types.error_message2


class IndexNotReadyException_(TypedDict, closed=True):
    message: NotRequired["capo_iot.types.error_message2.ErrorMessage2"]
    """<p>The message for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IndexNotReadyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> IndexNotReadyException_:
    out: IndexNotReadyException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class IndexNotReadyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iot#IndexNotReadyException``."""

    code: str | None = "IndexNotReadyException"

    def __init__(self, data: IndexNotReadyException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IndexNotReadyException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "IndexNotReadyException":
        return cls(deserialize_json(data))
