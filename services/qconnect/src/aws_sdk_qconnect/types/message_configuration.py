"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class MessageConfiguration(TypedDict, closed=True):
    generate_filler_message: NotRequired["bool"]
    """<p>Generates a filler response when tool selection is <code>QUESTION</code>.</p>"""
    generate_chunked_message: NotRequired["bool"]
    """<p>Configuration for generating chunked messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageConfiguration) -> dict:
    out: dict = {}
    if "generate_filler_message" in value:
        out["generateFillerMessage"] = value["generate_filler_message"]
    if "generate_chunked_message" in value:
        out["generateChunkedMessage"] = value["generate_chunked_message"]
    return out


def deserialize_json(data: dict) -> MessageConfiguration:
    out: MessageConfiguration = {}  # type: ignore[typeddict-item]
    if "generateFillerMessage" in data:
        out["generate_filler_message"] = data["generateFillerMessage"]
    if "generateChunkedMessage" in data:
        out["generate_chunked_message"] = data["generateChunkedMessage"]
    return out
