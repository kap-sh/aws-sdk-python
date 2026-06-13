"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#CreateMssManifestConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.filter_configuration
    import aws_sdk_mediapackagev2.types.manifest_name
    import aws_sdk_mediapackagev2.types.mss_manifest_layout


class CreateMssManifestConfiguration(TypedDict):
    manifest_name: "aws_sdk_mediapackagev2.types.manifest_name.ManifestName"
    """<p>A short string that's appended to the endpoint URL to create a unique path to this MSS manifest. The manifest name must be unique within the origin endpoint and can contain letters, numbers, hyphens, and underscores.</p>"""
    manifest_window_seconds: NotRequired["int"]
    """<p>The total duration (in seconds) of the manifest window. This determines how much content is available in the manifest at any given time. The manifest window slides forward as new segments become available, maintaining a consistent duration of content. The minimum value is 30 seconds.</p>"""
    filter_configuration: NotRequired[
        "aws_sdk_mediapackagev2.types.filter_configuration.FilterConfiguration"
    ]
    manifest_layout: NotRequired[
        "aws_sdk_mediapackagev2.types.mss_manifest_layout.MssManifestLayout"
    ]
    """<p>Determines the layout format of the MSS manifest. This controls how the manifest is structured and presented to client players, affecting compatibility with different MSS-compatible devices and applications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMssManifestConfiguration) -> dict:
    out: dict = {}
    out["ManifestName"] = value["manifest_name"]
    if "manifest_window_seconds" in value:
        out["ManifestWindowSeconds"] = value["manifest_window_seconds"]
    if "filter_configuration" in value:
        import aws_sdk_mediapackagev2.types.filter_configuration

        out["FilterConfiguration"] = (
            aws_sdk_mediapackagev2.types.filter_configuration.serialize_json(
                value["filter_configuration"]
            )
        )
    if "manifest_layout" in value:
        import aws_sdk_mediapackagev2.types.mss_manifest_layout

        out["ManifestLayout"] = (
            aws_sdk_mediapackagev2.types.mss_manifest_layout.serialize_json(
                value["manifest_layout"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateMssManifestConfiguration:
    out: CreateMssManifestConfiguration = {}  # type: ignore[typeddict-item]
    if "ManifestName" in data:
        out["manifest_name"] = data["ManifestName"]
    else:
        raise DeserializationError(
            "CreateMssManifestConfiguration.manifest_name required"
        )
    if "ManifestWindowSeconds" in data:
        out["manifest_window_seconds"] = data["ManifestWindowSeconds"]
    if "FilterConfiguration" in data:
        import aws_sdk_mediapackagev2.types.filter_configuration

        out["filter_configuration"] = (
            aws_sdk_mediapackagev2.types.filter_configuration.deserialize_json(
                data["FilterConfiguration"]
            )
        )
    if "ManifestLayout" in data:
        import aws_sdk_mediapackagev2.types.mss_manifest_layout

        out["manifest_layout"] = (
            aws_sdk_mediapackagev2.types.mss_manifest_layout.deserialize_json(
                data["ManifestLayout"]
            )
        )
    return out
