"""Generated from Smithy shape ``com.amazonaws.ram#TagPolicyViolationException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ram.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_ram.types.string


class TagPolicyViolationException_(TypedDict):
    message: "aws_sdk_ram.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: TagPolicyViolationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TagPolicyViolationException_:
    out: TagPolicyViolationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("TagPolicyViolationException_.message required")
    return out


class TagPolicyViolationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ram#TagPolicyViolationException``."""

    code: str | None = "TagPolicyViolationException"

    def __init__(self, data: TagPolicyViolationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TagPolicyViolationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "TagPolicyViolationException":
        return cls(deserialize_json(data))
