"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InlineAgentFilePart``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent_runtime._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.output_files


class InlineAgentFilePart(TypedDict):
    files: NotRequired["aws_sdk_bedrock_agent_runtime.types.output_files.OutputFiles"]
    """<p>Files containing intermediate response for the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InlineAgentFilePart) -> dict:
    out: dict = {}
    if "files" in value:
        import aws_sdk_bedrock_agent_runtime.types.output_files

        out["files"] = aws_sdk_bedrock_agent_runtime.types.output_files.serialize_json(
            value["files"]
        )
    return out


def deserialize_json(data: dict) -> InlineAgentFilePart:
    out: InlineAgentFilePart = {}  # type: ignore[typeddict-item]
    if "files" in data:
        import aws_sdk_bedrock_agent_runtime.types.output_files

        out["files"] = (
            aws_sdk_bedrock_agent_runtime.types.output_files.deserialize_json(
                data["files"]
            )
        )
    return out


def serialize_event_json(value: InlineAgentFilePart) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "files"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> InlineAgentFilePart:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: InlineAgentFilePart = {}  # type: ignore[typeddict-item]
    return out
