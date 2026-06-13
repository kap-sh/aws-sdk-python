"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#MessageStopEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.stop_reason


class MessageStopEvent(TypedDict):
    stop_reason: "aws_sdk_bedrock_runtime.types.stop_reason.StopReason"
    """<p>The reason why the model stopped generating output.</p>"""
    additional_model_response_fields: NotRequired["object"]
    """<p>The additional model response fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageStopEvent) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_runtime.types.stop_reason

    out["stopReason"] = aws_sdk_bedrock_runtime.types.stop_reason.serialize_json(
        value["stop_reason"]
    )
    if "additional_model_response_fields" in value:
        out["additionalModelResponseFields"] = value["additional_model_response_fields"]
    return out


def deserialize_json(data: dict) -> MessageStopEvent:
    out: MessageStopEvent = {}  # type: ignore[typeddict-item]
    if "stopReason" in data:
        import aws_sdk_bedrock_runtime.types.stop_reason

        out["stop_reason"] = aws_sdk_bedrock_runtime.types.stop_reason.deserialize_json(
            data["stopReason"]
        )
    else:
        raise DeserializationError("MessageStopEvent.stop_reason required")
    if "additionalModelResponseFields" in data:
        out["additional_model_response_fields"] = data["additionalModelResponseFields"]
    return out
