"""Generated from Smithy shape ``com.amazonaws.xray#LockoutPreventionException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_xray.errors import ServiceError

if TYPE_CHECKING:
    import capo_xray.types.error_message


class LockoutPreventionException_(TypedDict, closed=True):
    message: NotRequired["capo_xray.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: LockoutPreventionException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> LockoutPreventionException_:
    out: LockoutPreventionException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class LockoutPreventionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.xray#LockoutPreventionException``."""

    code: str | None = "LockoutPreventionException"

    def __init__(self, data: LockoutPreventionException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LockoutPreventionException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "LockoutPreventionException":
        return cls(deserialize_json(data))
