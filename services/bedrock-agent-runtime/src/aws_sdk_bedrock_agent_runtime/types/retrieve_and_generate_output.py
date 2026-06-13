"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrieveAndGenerateOutput``."""

from typing import TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError


class RetrieveAndGenerateOutput(TypedDict):
    text: "str"
    """<p>The response generated from querying the knowledge base.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrieveAndGenerateOutput) -> dict:
    out: dict = {}
    out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> RetrieveAndGenerateOutput:
    out: RetrieveAndGenerateOutput = {}  # type: ignore[typeddict-item]
    if "text" in data:
        out["text"] = data["text"]
    else:
        raise DeserializationError("RetrieveAndGenerateOutput.text required")
    return out
