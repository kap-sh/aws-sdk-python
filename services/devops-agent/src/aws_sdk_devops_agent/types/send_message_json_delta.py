"""Generated from Smithy shape ``com.amazonaws.devopsagent#SendMessageJsonDelta``."""

from typing import TypedDict

from typing_extensions import NotRequired


class SendMessageJsonDelta(TypedDict):
    partial_json: NotRequired["str"]
    """<p>Partial JSON string</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendMessageJsonDelta) -> dict:
    out: dict = {}
    if "partial_json" in value:
        out["partialJson"] = value["partial_json"]
    return out


def deserialize_json(data: dict) -> SendMessageJsonDelta:
    out: SendMessageJsonDelta = {}  # type: ignore[typeddict-item]
    if "partialJson" in data:
        out["partial_json"] = data["partialJson"]
    return out
