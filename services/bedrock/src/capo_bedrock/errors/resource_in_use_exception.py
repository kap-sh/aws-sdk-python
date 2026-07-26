"""Generated from Smithy shape ``com.amazonaws.bedrock#ResourceInUseException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import ServiceError

if TYPE_CHECKING:
    import capo_bedrock.types.non_blank_string


class ResourceInUseException_(TypedDict, closed=True):
    message: NotRequired["capo_bedrock.types.non_blank_string.NonBlankString"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceInUseException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceInUseException_:
    out: ResourceInUseException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ResourceInUseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrock#ResourceInUseException``."""

    code: str | None = "ResourceInUseException"

    def __init__(self, data: ResourceInUseException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceInUseException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceInUseException":
        return cls(deserialize_json(data))
