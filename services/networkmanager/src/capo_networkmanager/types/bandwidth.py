"""Generated from Smithy shape ``com.amazonaws.networkmanager#Bandwidth``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.integer


class Bandwidth(TypedDict, closed=True):
    upload_speed: NotRequired["capo_networkmanager.types.integer.Integer"]
    """<p>Upload speed in Mbps.</p>"""
    download_speed: NotRequired["capo_networkmanager.types.integer.Integer"]
    """<p>Download speed in Mbps.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Bandwidth) -> dict:
    out: dict = {}
    if "upload_speed" in value:
        out["UploadSpeed"] = value["upload_speed"]
    if "download_speed" in value:
        out["DownloadSpeed"] = value["download_speed"]
    return out


def deserialize_json(data: dict) -> Bandwidth:
    out: Bandwidth = {}  # type: ignore[typeddict-item]
    if "UploadSpeed" in data:
        out["upload_speed"] = data["UploadSpeed"]
    if "DownloadSpeed" in data:
        out["download_speed"] = data["DownloadSpeed"]
    return out
