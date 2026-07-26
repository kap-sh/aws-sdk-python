"""Generated from Smithy shape ``com.amazonaws.clouddirectory#UnsupportedIndexTypeException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_clouddirectory.errors import ServiceError

if TYPE_CHECKING:
    import capo_clouddirectory.types.exception_message


class UnsupportedIndexTypeException_(TypedDict, closed=True):
    message: NotRequired["capo_clouddirectory.types.exception_message.ExceptionMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: UnsupportedIndexTypeException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnsupportedIndexTypeException_:
    out: UnsupportedIndexTypeException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class UnsupportedIndexTypeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.clouddirectory#UnsupportedIndexTypeException``."""

    code: str | None = "UnsupportedIndexTypeException"

    def __init__(self, data: UnsupportedIndexTypeException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedIndexTypeException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "UnsupportedIndexTypeException":
        return cls(deserialize_json(data))
