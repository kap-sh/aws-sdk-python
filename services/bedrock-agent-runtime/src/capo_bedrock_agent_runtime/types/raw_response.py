"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RawResponse``."""

from typing_extensions import NotRequired, TypedDict


class RawResponse(TypedDict, closed=True):
    content: NotRequired["str"]
    """<p>The foundation model's raw output content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RawResponse) -> dict:
    out: dict = {}
    if "content" in value:
        out["content"] = value["content"]
    return out


def deserialize_json(data: dict) -> RawResponse:
    out: RawResponse = {}  # type: ignore[typeddict-item]
    if "content" in data:
        out["content"] = data["content"]
    return out
