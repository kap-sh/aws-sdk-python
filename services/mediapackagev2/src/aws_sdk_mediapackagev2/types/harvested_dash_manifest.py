"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#HarvestedDashManifest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.resource_name


class HarvestedDashManifest(TypedDict):
    manifest_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the harvested DASH manifest.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarvestedDashManifest) -> dict:
    out: dict = {}
    out["ManifestName"] = value["manifest_name"]
    return out


def deserialize_json(data: dict) -> HarvestedDashManifest:
    out: HarvestedDashManifest = {}  # type: ignore[typeddict-item]
    if "ManifestName" in data:
        out["manifest_name"] = data["ManifestName"]
    else:
        raise DeserializationError("HarvestedDashManifest.manifest_name required")
    return out
