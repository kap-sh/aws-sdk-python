"""Generated from Smithy shape ``com.amazonaws.panorama#AlternateSoftwareMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_panorama.types.version


class AlternateSoftwareMetadata(TypedDict, closed=True):
    version: NotRequired["aws_sdk_panorama.types.version.Version"]
    """<p>The appliance software version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AlternateSoftwareMetadata) -> dict:
    out: dict = {}
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_json(data: dict) -> AlternateSoftwareMetadata:
    out: AlternateSoftwareMetadata = {}  # type: ignore[typeddict-item]
    if "Version" in data:
        out["version"] = data["Version"]
    return out
