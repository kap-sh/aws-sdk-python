"""Generated from Smithy shape ``com.amazonaws.efs#MountTargetConflict``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_efs.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_efs.types.error_code
    import capo_efs.types.error_message


class MountTargetConflict_(TypedDict, closed=True):
    error_code: "capo_efs.types.error_code.ErrorCode"
    message: NotRequired["capo_efs.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: MountTargetConflict_) -> dict:
    out: dict = {}
    out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> MountTargetConflict_:
    out: MountTargetConflict_ = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    else:
        raise DeserializationError("MountTargetConflict_.error_code required")
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class MountTargetConflict(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.efs#MountTargetConflict``."""

    code: str | None = "MountTargetConflict"

    def __init__(self, data: MountTargetConflict_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MountTargetConflict",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "MountTargetConflict":
        return cls(deserialize_json(data))
