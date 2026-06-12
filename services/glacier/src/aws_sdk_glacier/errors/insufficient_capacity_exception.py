"""Generated from Smithy shape ``com.amazonaws.glacier#InsufficientCapacityException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glacier.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string


class InsufficientCapacityException_(TypedDict):
    type: NotRequired["aws_sdk_glacier.types.string.string"]
    code: NotRequired["aws_sdk_glacier.types.string.string"]
    message: NotRequired["aws_sdk_glacier.types.string.string"]


# --- restJson1 ser/de ---
def serialize_json(value: InsufficientCapacityException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InsufficientCapacityException_:
    out: InsufficientCapacityException_ = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    if "code" in data:
        out["code"] = data["code"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InsufficientCapacityException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glacier#InsufficientCapacityException``."""

    code: str | None = "InsufficientCapacityException"

    def __init__(self, data: InsufficientCapacityException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InsufficientCapacityException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InsufficientCapacityException":
        return cls(deserialize_json(data))
