"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenJobAsset``."""

from typing import TypedDict

from typing_extensions import NotRequired


class CodegenJobAsset(TypedDict):
    download_url: NotRequired["str"]
    """<p>The URL to use to access the asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodegenJobAsset) -> dict:
    out: dict = {}
    if "download_url" in value:
        out["downloadUrl"] = value["download_url"]
    return out


def deserialize_json(data: dict) -> CodegenJobAsset:
    out: CodegenJobAsset = {}  # type: ignore[typeddict-item]
    if "downloadUrl" in data:
        out["download_url"] = data["downloadUrl"]
    return out
