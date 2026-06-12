"""Generated from Smithy shape ``com.amazonaws.controltower#Region``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_controltower.types.region_name


class Region(TypedDict):
    name: NotRequired["aws_sdk_controltower.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Region) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> Region:
    out: Region = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    return out
