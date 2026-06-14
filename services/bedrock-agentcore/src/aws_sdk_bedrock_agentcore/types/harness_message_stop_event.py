"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessMessageStopEvent``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.harness_stop_reason


class HarnessMessageStopEvent(TypedDict):
    stop_reason: "aws_sdk_bedrock_agentcore.types.harness_stop_reason.HarnessStopReason"
    """<p>The reason the agent stopped generating.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessMessageStopEvent) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.harness_stop_reason

    out["stopReason"] = (
        aws_sdk_bedrock_agentcore.types.harness_stop_reason.serialize_json(
            value["stop_reason"]
        )
    )
    return out


def deserialize_json(data: dict) -> HarnessMessageStopEvent:
    out: HarnessMessageStopEvent = {}  # type: ignore[typeddict-item]
    if "stopReason" in data:
        import aws_sdk_bedrock_agentcore.types.harness_stop_reason

        out["stop_reason"] = (
            aws_sdk_bedrock_agentcore.types.harness_stop_reason.deserialize_json(
                data["stopReason"]
            )
        )
    else:
        raise DeserializationError("HarnessMessageStopEvent.stop_reason required")
    return out
