"""Generated from Smithy shape ``com.amazonaws.mediatailor#Bumper``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string


class Bumper(TypedDict, closed=True):
    end_url: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The URL for the end bumper asset.</p>"""
    start_url: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The URL for the start bumper asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Bumper) -> dict:
    out: dict = {}
    if "end_url" in value:
        out["EndUrl"] = value["end_url"]
    if "start_url" in value:
        out["StartUrl"] = value["start_url"]
    return out


def deserialize_json(data: dict) -> Bumper:
    out: Bumper = {}  # type: ignore[typeddict-item]
    if "EndUrl" in data:
        out["end_url"] = data["EndUrl"]
    if "StartUrl" in data:
        out["start_url"] = data["StartUrl"]
    return out
