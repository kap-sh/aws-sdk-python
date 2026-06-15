"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AccessDeniedException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.non_blank_string


class AccessDeniedException_(TypedDict):
    message: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.non_blank_string.NonBlankString"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: AccessDeniedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AccessDeniedException``."""

    code: str | None = "AccessDeniedException"

    def __init__(self, data: AccessDeniedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccessDeniedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "AccessDeniedException":
        return cls(deserialize_json(data))
