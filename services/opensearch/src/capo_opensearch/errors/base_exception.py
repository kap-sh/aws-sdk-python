"""Generated from Smithy shape ``com.amazonaws.opensearch#BaseException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_opensearch.errors import ServiceError

if TYPE_CHECKING:
    import capo_opensearch.types.error_message


class BaseException_(TypedDict, closed=True):
    message: NotRequired["capo_opensearch.types.error_message.ErrorMessage"]
    """<p>A description of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BaseException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BaseException_:
    out: BaseException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class BaseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.opensearch#BaseException``."""

    code: str | None = "BaseException"

    def __init__(self, data: BaseException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BaseException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "BaseException":
        return cls(deserialize_json(data))
