"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CustomDocumentIdentifier``."""

from typing import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError


class CustomDocumentIdentifier(TypedDict):
    id: "str"
    """<p>The identifier of the document to ingest into a custom data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomDocumentIdentifier) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> CustomDocumentIdentifier:
    out: CustomDocumentIdentifier = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CustomDocumentIdentifier.id required")
    return out
