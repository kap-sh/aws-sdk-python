"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ProbeResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__list_of_track_mapping
    import capo_mediaconvert.types.container
    import capo_mediaconvert.types.metadata


class ProbeResult(TypedDict, closed=True):
    container: NotRequired["capo_mediaconvert.types.container.Container"]
    """The container of your media file. This information helps you understand the overall structure and details of your media, including format, duration, and track layout."""
    metadata: NotRequired["capo_mediaconvert.types.metadata.Metadata"]
    """Metadata and other file information."""
    track_mappings: NotRequired[
        "capo_mediaconvert.types.__list_of_track_mapping.__listOfTrackMapping"
    ]
    """An array containing track mapping information."""


# --- restJson1 ser/de ---
def serialize_json(value: ProbeResult) -> dict:
    out: dict = {}
    if "container" in value:
        import capo_mediaconvert.types.container

        out["container"] = capo_mediaconvert.types.container.serialize_json(
            value["container"]
        )
    if "metadata" in value:
        import capo_mediaconvert.types.metadata

        out["metadata"] = capo_mediaconvert.types.metadata.serialize_json(
            value["metadata"]
        )
    if "track_mappings" in value:
        import capo_mediaconvert.types.__list_of_track_mapping

        out["trackMappings"] = (
            capo_mediaconvert.types.__list_of_track_mapping.serialize_json(
                value["track_mappings"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProbeResult:
    out: ProbeResult = {}  # type: ignore[typeddict-item]
    if "container" in data:
        import capo_mediaconvert.types.container

        out["container"] = capo_mediaconvert.types.container.deserialize_json(
            data["container"]
        )
    if "metadata" in data:
        import capo_mediaconvert.types.metadata

        out["metadata"] = capo_mediaconvert.types.metadata.deserialize_json(
            data["metadata"]
        )
    if "trackMappings" in data:
        import capo_mediaconvert.types.__list_of_track_mapping

        out["track_mappings"] = (
            capo_mediaconvert.types.__list_of_track_mapping.deserialize_json(
                data["trackMappings"]
            )
        )
    return out
