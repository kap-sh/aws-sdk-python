"""Generated from Smithy shape ``com.amazonaws.bedrockagent#TextContentDoc``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.data


class TextContentDoc(TypedDict, closed=True):
    data: "aws_sdk_bedrock_agent.types.data.Data"
    """<p>The text of the content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextContentDoc) -> dict:
    out: dict = {}
    out["data"] = value["data"]
    return out


def deserialize_json(data: dict) -> TextContentDoc:
    out: TextContentDoc = {}  # type: ignore[typeddict-item]
    if "data" in data:
        out["data"] = data["data"]
    else:
        raise DeserializationError("TextContentDoc.data required")
    return out
