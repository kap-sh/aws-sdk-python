"""Generated from Smithy shape ``com.amazonaws.wickr#ShredderSettings``."""

from typing_extensions import NotRequired, TypedDict


class ShredderSettings(TypedDict, closed=True):
    can_process_manually: NotRequired["bool"]
    """<p>Specifies whether users can manually trigger the shredder to delete content.</p>"""
    intensity: NotRequired["int"]
    """<p>Controls the rate (MB/minute) at which the shredder function runs on clients. Valid Values: Must be one of [0, 20, 60, 100].</p> <note> <p>A higher intensity setting could lead to higher battery usage on mobile devices.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ShredderSettings) -> dict:
    out: dict = {}
    if "can_process_manually" in value:
        out["canProcessManually"] = value["can_process_manually"]
    if "intensity" in value:
        out["intensity"] = value["intensity"]
    return out


def deserialize_json(data: dict) -> ShredderSettings:
    out: ShredderSettings = {}  # type: ignore[typeddict-item]
    if "canProcessManually" in data:
        out["can_process_manually"] = data["canProcessManually"]
    if "intensity" in data:
        out["intensity"] = data["intensity"]
    return out
