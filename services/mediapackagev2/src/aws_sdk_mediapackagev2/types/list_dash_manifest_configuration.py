"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ListDashManifestConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.resource_name


class ListDashManifestConfiguration(TypedDict):
    manifest_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>A short string that's appended to the endpoint URL. The manifest name creates a unique path to this endpoint. If you don't enter a value, MediaPackage uses the default manifest name, index. </p>"""
    url: NotRequired["str"]
    """<p>The egress domain URL for stream delivery from MediaPackage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDashManifestConfiguration) -> dict:
    out: dict = {}
    out["ManifestName"] = value["manifest_name"]
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_json(data: dict) -> ListDashManifestConfiguration:
    out: ListDashManifestConfiguration = {}  # type: ignore[typeddict-item]
    if "ManifestName" in data:
        out["manifest_name"] = data["ManifestName"]
    else:
        raise DeserializationError(
            "ListDashManifestConfiguration.manifest_name required"
        )
    if "Url" in data:
        out["url"] = data["Url"]
    return out
