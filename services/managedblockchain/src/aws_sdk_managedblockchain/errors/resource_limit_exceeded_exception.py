"""Generated from Smithy shape ``com.amazonaws.managedblockchain#ResourceLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_managedblockchain.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.string


class ResourceLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_managedblockchain.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceLimitExceededException_:
    out: ResourceLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ResourceLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.managedblockchain#ResourceLimitExceededException``."""

    code: str | None = "ResourceLimitExceededException"

    def __init__(self, data: ResourceLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceLimitExceededException":
        return cls(deserialize_json(data))
