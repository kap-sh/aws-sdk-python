"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessToolUseBlockDelta``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.sensitive_text


class HarnessToolUseBlockDelta(TypedDict, closed=True):
    input: "aws_sdk_bedrock_agentcore.types.sensitive_text.SensitiveText"
    """<p>The partial JSON input for the tool call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessToolUseBlockDelta) -> dict:
    out: dict = {}
    out["input"] = value["input"]
    return out


def deserialize_json(data: dict) -> HarnessToolUseBlockDelta:
    out: HarnessToolUseBlockDelta = {}  # type: ignore[typeddict-item]
    if "input" in data:
        out["input"] = data["input"]
    else:
        raise DeserializationError("HarnessToolUseBlockDelta.input required")
    return out
