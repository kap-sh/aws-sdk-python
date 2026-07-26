"""Generated from Smithy shape ``com.amazonaws.mediaconnect#NdiSourceInfo``."""

from typing_extensions import NotRequired, TypedDict


class NdiSourceInfo(TypedDict, closed=True):
    source_name: NotRequired["str"]
    """<p> The name of the upstream NDI sender. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NdiSourceInfo) -> dict:
    out: dict = {}
    if "source_name" in value:
        out["sourceName"] = value["source_name"]
    return out


def deserialize_json(data: dict) -> NdiSourceInfo:
    out: NdiSourceInfo = {}  # type: ignore[typeddict-item]
    if "sourceName" in data:
        out["source_name"] = data["sourceName"]
    return out
