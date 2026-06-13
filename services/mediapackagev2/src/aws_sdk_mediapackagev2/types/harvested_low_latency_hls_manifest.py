"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#HarvestedLowLatencyHlsManifest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.resource_name


class HarvestedLowLatencyHlsManifest(TypedDict):
    manifest_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the harvested Low-Latency HLS manifest.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarvestedLowLatencyHlsManifest) -> dict:
    out: dict = {}
    out["ManifestName"] = value["manifest_name"]
    return out


def deserialize_json(data: dict) -> HarvestedLowLatencyHlsManifest:
    out: HarvestedLowLatencyHlsManifest = {}  # type: ignore[typeddict-item]
    if "ManifestName" in data:
        out["manifest_name"] = data["ManifestName"]
    else:
        raise DeserializationError(
            "HarvestedLowLatencyHlsManifest.manifest_name required"
        )
    return out
