"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DuplicateIdException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agentcore.errors import ServiceError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.non_blank_string

class DuplicateIdException_(TypedDict):
    message: NotRequired["aws_sdk_bedrock_agentcore.types.non_blank_string.NonBlankString"]

# --- restJson1 ser/de ---
def serialize_json(value: DuplicateIdException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DuplicateIdException_:
    out: DuplicateIdException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class DuplicateIdException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockagentcore#DuplicateIdException``."""
    code: str | None = 'DuplicateIdException'

    def __init__(self, data: DuplicateIdException_):
        super().__init__('client', is_throttling_error=False, is_retryable=False, code='DuplicateIdException')
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "DuplicateIdException":
        return cls(deserialize_json(data))