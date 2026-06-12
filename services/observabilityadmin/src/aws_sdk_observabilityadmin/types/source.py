"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#Source``."""

from typing import TypedDict

from typing_extensions import NotRequired


class Source(TypedDict):
    type: NotRequired["str"]
    """<p>The plugin name of the source, such as <code>cloudwatch_logs</code> or <code>s3</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Source) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> Source:
    out: Source = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
