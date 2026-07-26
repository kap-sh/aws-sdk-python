"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#TagsPerResourceExceededLimitException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis_video.errors import ServiceError

if TYPE_CHECKING:
    import capo_kinesis_video.types.error_message


class TagsPerResourceExceededLimitException_(TypedDict, closed=True):
    message: NotRequired["capo_kinesis_video.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: TagsPerResourceExceededLimitException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TagsPerResourceExceededLimitException_:
    out: TagsPerResourceExceededLimitException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class TagsPerResourceExceededLimitException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesisvideo#TagsPerResourceExceededLimitException``."""

    code: str | None = "TagsPerResourceExceededLimitException"

    def __init__(self, data: TagsPerResourceExceededLimitException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TagsPerResourceExceededLimitException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "TagsPerResourceExceededLimitException":
        return cls(deserialize_json(data))
