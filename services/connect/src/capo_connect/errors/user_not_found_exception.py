"""Generated from Smithy shape ``com.amazonaws.connect#UserNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import ServiceError

if TYPE_CHECKING:
    import capo_connect.types.message


class UserNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_connect.types.message.Message"]


# --- restJson1 ser/de ---
def serialize_json(value: UserNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UserNotFoundException_:
    out: UserNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class UserNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connect#UserNotFoundException``."""

    code: str | None = "UserNotFoundException"

    def __init__(self, data: UserNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UserNotFoundException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "UserNotFoundException":
        return cls(deserialize_json(data))
