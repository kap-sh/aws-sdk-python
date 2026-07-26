"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#CreatePresetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_transcoder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.audio_parameters
    import capo_elastic_transcoder.types.description
    import capo_elastic_transcoder.types.name
    import capo_elastic_transcoder.types.preset_container
    import capo_elastic_transcoder.types.thumbnails
    import capo_elastic_transcoder.types.video_parameters


class CreatePresetRequest(TypedDict, closed=True):
    name: "capo_elastic_transcoder.types.name.Name"
    """<p>The name of the preset. We recommend that the name be unique within the AWS account, but uniqueness is not enforced.</p>"""
    description: NotRequired["capo_elastic_transcoder.types.description.Description"]
    """<p>A description of the preset.</p>"""
    container: "capo_elastic_transcoder.types.preset_container.PresetContainer"
    """<p>The container type for the output file. Valid values include <code>flac</code>, <code>flv</code>, <code>fmp4</code>, <code>gif</code>, <code>mp3</code>, <code>mp4</code>, <code>mpg</code>, <code>mxf</code>, <code>oga</code>, <code>ogg</code>, <code>ts</code>, and <code>webm</code>.</p>"""
    video: NotRequired["capo_elastic_transcoder.types.video_parameters.VideoParameters"]
    """<p>A section of the request body that specifies the video parameters.</p>"""
    audio: NotRequired["capo_elastic_transcoder.types.audio_parameters.AudioParameters"]
    """<p>A section of the request body that specifies the audio parameters.</p>"""
    thumbnails: NotRequired["capo_elastic_transcoder.types.thumbnails.Thumbnails"]
    """<p>A section of the request body that specifies the thumbnail parameters, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePresetRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["Container"] = value["container"]
    if "video" in value:
        import capo_elastic_transcoder.types.video_parameters

        out["Video"] = capo_elastic_transcoder.types.video_parameters.serialize_json(
            value["video"]
        )
    if "audio" in value:
        import capo_elastic_transcoder.types.audio_parameters

        out["Audio"] = capo_elastic_transcoder.types.audio_parameters.serialize_json(
            value["audio"]
        )
    if "thumbnails" in value:
        import capo_elastic_transcoder.types.thumbnails

        out["Thumbnails"] = capo_elastic_transcoder.types.thumbnails.serialize_json(
            value["thumbnails"]
        )
    return out


def deserialize_json(data: dict) -> CreatePresetRequest:
    out: CreatePresetRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreatePresetRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Container" in data:
        out["container"] = data["Container"]
    else:
        raise DeserializationError("CreatePresetRequest.container required")
    if "Video" in data:
        import capo_elastic_transcoder.types.video_parameters

        out["video"] = capo_elastic_transcoder.types.video_parameters.deserialize_json(
            data["Video"]
        )
    if "Audio" in data:
        import capo_elastic_transcoder.types.audio_parameters

        out["audio"] = capo_elastic_transcoder.types.audio_parameters.deserialize_json(
            data["Audio"]
        )
    if "Thumbnails" in data:
        import capo_elastic_transcoder.types.thumbnails

        out["thumbnails"] = capo_elastic_transcoder.types.thumbnails.deserialize_json(
            data["Thumbnails"]
        )
    return out
