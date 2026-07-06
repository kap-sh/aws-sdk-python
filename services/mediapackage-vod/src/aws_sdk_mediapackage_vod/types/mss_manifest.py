"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#MssManifest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackage_vod.types.__string
    import aws_sdk_mediapackage_vod.types.stream_selection


class MssManifest(TypedDict, closed=True):
    manifest_name: NotRequired["aws_sdk_mediapackage_vod.types.__string.__string"]
    """An optional string to include in the name of the manifest."""
    stream_selection: NotRequired[
        "aws_sdk_mediapackage_vod.types.stream_selection.StreamSelection"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: MssManifest) -> dict:
    out: dict = {}
    if "manifest_name" in value:
        out["manifestName"] = value["manifest_name"]
    if "stream_selection" in value:
        import aws_sdk_mediapackage_vod.types.stream_selection

        out["streamSelection"] = (
            aws_sdk_mediapackage_vod.types.stream_selection.serialize_json(
                value["stream_selection"]
            )
        )
    return out


def deserialize_json(data: dict) -> MssManifest:
    out: MssManifest = {}  # type: ignore[typeddict-item]
    if "manifestName" in data:
        out["manifest_name"] = data["manifestName"]
    if "streamSelection" in data:
        import aws_sdk_mediapackage_vod.types.stream_selection

        out["stream_selection"] = (
            aws_sdk_mediapackage_vod.types.stream_selection.deserialize_json(
                data["streamSelection"]
            )
        )
    return out
