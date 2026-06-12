"""Generated from Smithy shape ``com.amazonaws.groundstation#AntennaDemodDecodeDetails``."""

from typing import TypedDict
from typing_extensions import NotRequired

class AntennaDemodDecodeDetails(TypedDict):
    output_node: NotRequired["str"]
    """<p>Name of an antenna demod decode output node used in a contact.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AntennaDemodDecodeDetails) -> dict:
    out: dict = {}
    if "output_node" in value:
        out["outputNode"] = value["output_node"]
    return out


def deserialize_json(data: dict) -> AntennaDemodDecodeDetails:
    out: AntennaDemodDecodeDetails = {}  # type: ignore[typeddict-item]
    if "outputNode" in data:
        out["output_node"] = data["outputNode"]
    return out