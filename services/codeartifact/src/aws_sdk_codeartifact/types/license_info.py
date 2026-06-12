"""Generated from Smithy shape ``com.amazonaws.codeartifact#LicenseInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.string


class LicenseInfo(TypedDict):
    name: NotRequired["aws_sdk_codeartifact.types.string.String"]
    """<p> Name of the license. </p>"""
    url: NotRequired["aws_sdk_codeartifact.types.string.String"]
    """<p> The URL for license data. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LicenseInfo) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "url" in value:
        out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> LicenseInfo:
    out: LicenseInfo = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "url" in data:
        out["url"] = data["url"]
    return out
