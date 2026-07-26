"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#SourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.selected_video_streams


class SourceConfiguration(TypedDict, closed=True):
    selected_video_streams: NotRequired[
        "capo_chime_sdk_media_pipelines.types.selected_video_streams.SelectedVideoStreams"
    ]
    """<p>The selected video streams for a specified media pipeline. The number of video streams can't exceed 25.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceConfiguration) -> dict:
    out: dict = {}
    if "selected_video_streams" in value:
        import capo_chime_sdk_media_pipelines.types.selected_video_streams

        out["SelectedVideoStreams"] = (
            capo_chime_sdk_media_pipelines.types.selected_video_streams.serialize_json(
                value["selected_video_streams"]
            )
        )
    return out


def deserialize_json(data: dict) -> SourceConfiguration:
    out: SourceConfiguration = {}  # type: ignore[typeddict-item]
    if "SelectedVideoStreams" in data:
        import capo_chime_sdk_media_pipelines.types.selected_video_streams

        out["selected_video_streams"] = (
            capo_chime_sdk_media_pipelines.types.selected_video_streams.deserialize_json(
                data["SelectedVideoStreams"]
            )
        )
    return out
