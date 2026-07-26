"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ThrottledException``."""

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import ServiceError


class ThrottledException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ThrottledException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ThrottledException_:
    out: ThrottledException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ThrottledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ThrottledException``."""

    code: str | None = "ThrottledException"

    def __init__(self, data: ThrottledException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=True,
            code="ThrottledException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ThrottledException":
        return cls(deserialize_json(data))
