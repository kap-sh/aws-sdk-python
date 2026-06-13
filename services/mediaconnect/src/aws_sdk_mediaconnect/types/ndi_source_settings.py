"""Generated from Smithy shape ``com.amazonaws.mediaconnect#NdiSourceSettings``."""

from typing import TypedDict

from typing_extensions import NotRequired


class NdiSourceSettings(TypedDict):
    source_name: NotRequired["str"]
    """<p> The exact name of an existing NDI sender that's registered with your discovery server. If included, the format of this name must be <code>MACHINENAME (ProgramName)</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NdiSourceSettings) -> dict:
    out: dict = {}
    if "source_name" in value:
        out["sourceName"] = value["source_name"]
    return out


def deserialize_json(data: dict) -> NdiSourceSettings:
    out: NdiSourceSettings = {}  # type: ignore[typeddict-item]
    if "sourceName" in data:
        out["source_name"] = data["sourceName"]
    return out
