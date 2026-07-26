"""Generated from Smithy shape ``com.amazonaws.clouddirectory#CannotListParentOfRootException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_clouddirectory.errors import ServiceError

if TYPE_CHECKING:
    import capo_clouddirectory.types.exception_message


class CannotListParentOfRootException_(TypedDict, closed=True):
    message: NotRequired["capo_clouddirectory.types.exception_message.ExceptionMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: CannotListParentOfRootException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> CannotListParentOfRootException_:
    out: CannotListParentOfRootException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class CannotListParentOfRootException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.clouddirectory#CannotListParentOfRootException``."""

    code: str | None = "CannotListParentOfRootException"

    def __init__(self, data: CannotListParentOfRootException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CannotListParentOfRootException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "CannotListParentOfRootException":
        return cls(deserialize_json(data))
