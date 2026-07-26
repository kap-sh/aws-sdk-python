"""Generated from Smithy shape ``com.amazonaws.managedblockchain#IllegalActionException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_managedblockchain.errors import ServiceError

if TYPE_CHECKING:
    import capo_managedblockchain.types.string


class IllegalActionException_(TypedDict, closed=True):
    message: NotRequired["capo_managedblockchain.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: IllegalActionException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> IllegalActionException_:
    out: IllegalActionException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class IllegalActionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.managedblockchain#IllegalActionException``."""

    code: str | None = "IllegalActionException"

    def __init__(self, data: IllegalActionException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IllegalActionException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "IllegalActionException":
        return cls(deserialize_json(data))
