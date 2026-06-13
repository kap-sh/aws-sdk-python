"""Generated from Smithy shape ``com.amazonaws.qconnect#GetAssistantResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.assistant_data


class GetAssistantResponse(TypedDict):
    assistant: NotRequired["aws_sdk_qconnect.types.assistant_data.AssistantData"]
    """<p>Information about the assistant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssistantResponse) -> dict:
    out: dict = {}
    if "assistant" in value:
        import aws_sdk_qconnect.types.assistant_data

        out["assistant"] = aws_sdk_qconnect.types.assistant_data.serialize_json(
            value["assistant"]
        )
    return out


def deserialize_json(data: dict) -> GetAssistantResponse:
    out: GetAssistantResponse = {}  # type: ignore[typeddict-item]
    if "assistant" in data:
        import aws_sdk_qconnect.types.assistant_data

        out["assistant"] = aws_sdk_qconnect.types.assistant_data.deserialize_json(
            data["assistant"]
        )
    return out
