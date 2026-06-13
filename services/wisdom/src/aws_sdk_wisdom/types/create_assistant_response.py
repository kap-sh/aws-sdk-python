"""Generated from Smithy shape ``com.amazonaws.wisdom#CreateAssistantResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.assistant_data


class CreateAssistantResponse(TypedDict):
    assistant: NotRequired["aws_sdk_wisdom.types.assistant_data.AssistantData"]
    """<p>Information about the assistant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssistantResponse) -> dict:
    out: dict = {}
    if "assistant" in value:
        import aws_sdk_wisdom.types.assistant_data

        out["assistant"] = aws_sdk_wisdom.types.assistant_data.serialize_json(
            value["assistant"]
        )
    return out


def deserialize_json(data: dict) -> CreateAssistantResponse:
    out: CreateAssistantResponse = {}  # type: ignore[typeddict-item]
    if "assistant" in data:
        import aws_sdk_wisdom.types.assistant_data

        out["assistant"] = aws_sdk_wisdom.types.assistant_data.deserialize_json(
            data["assistant"]
        )
    return out
