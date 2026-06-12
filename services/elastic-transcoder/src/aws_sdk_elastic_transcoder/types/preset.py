"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#Preset``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.audio_parameters
    import aws_sdk_elastic_transcoder.types.description
    import aws_sdk_elastic_transcoder.types.id
    import aws_sdk_elastic_transcoder.types.name
    import aws_sdk_elastic_transcoder.types.preset_container
    import aws_sdk_elastic_transcoder.types.preset_type
    import aws_sdk_elastic_transcoder.types.string
    import aws_sdk_elastic_transcoder.types.thumbnails
    import aws_sdk_elastic_transcoder.types.video_parameters


class Preset(TypedDict):
    id: NotRequired["aws_sdk_elastic_transcoder.types.id.Id"]
    """<p>Identifier for the new preset. You use this value to get settings for the preset or to delete it.</p>"""
    arn: NotRequired["aws_sdk_elastic_transcoder.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the preset.</p>"""
    name: NotRequired["aws_sdk_elastic_transcoder.types.name.Name"]
    """<p>The name of the preset.</p>"""
    description: NotRequired["aws_sdk_elastic_transcoder.types.description.Description"]
    """<p>A description of the preset.</p>"""
    container: NotRequired[
        "aws_sdk_elastic_transcoder.types.preset_container.PresetContainer"
    ]
    """<p>The container type for the output file. Valid values include <code>flac</code>, <code>flv</code>, <code>fmp4</code>, <code>gif</code>, <code>mp3</code>, <code>mp4</code>, <code>mpg</code>, <code>mxf</code>, <code>oga</code>, <code>ogg</code>, <code>ts</code>, and <code>webm</code>.</p>"""
    audio: NotRequired[
        "aws_sdk_elastic_transcoder.types.audio_parameters.AudioParameters"
    ]
    """<p>A section of the response body that provides information about the audio preset values.</p>"""
    video: NotRequired[
        "aws_sdk_elastic_transcoder.types.video_parameters.VideoParameters"
    ]
    """<p>A section of the response body that provides information about the video preset values.</p>"""
    thumbnails: NotRequired["aws_sdk_elastic_transcoder.types.thumbnails.Thumbnails"]
    """<p>A section of the response body that provides information about the thumbnail preset values, if any.</p>"""
    type: NotRequired["aws_sdk_elastic_transcoder.types.preset_type.PresetType"]
    """<p>Whether the preset is a default preset provided by Elastic Transcoder (<code>System</code>) or a preset that you have defined (<code>Custom</code>).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Preset) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "container" in value:
        out["Container"] = value["container"]
    if "audio" in value:
        import aws_sdk_elastic_transcoder.types.audio_parameters

        out["Audio"] = aws_sdk_elastic_transcoder.types.audio_parameters.serialize_json(
            value["audio"]
        )
    if "video" in value:
        import aws_sdk_elastic_transcoder.types.video_parameters

        out["Video"] = aws_sdk_elastic_transcoder.types.video_parameters.serialize_json(
            value["video"]
        )
    if "thumbnails" in value:
        import aws_sdk_elastic_transcoder.types.thumbnails

        out["Thumbnails"] = aws_sdk_elastic_transcoder.types.thumbnails.serialize_json(
            value["thumbnails"]
        )
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> Preset:
    out: Preset = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Container" in data:
        out["container"] = data["Container"]
    if "Audio" in data:
        import aws_sdk_elastic_transcoder.types.audio_parameters

        out["audio"] = (
            aws_sdk_elastic_transcoder.types.audio_parameters.deserialize_json(
                data["Audio"]
            )
        )
    if "Video" in data:
        import aws_sdk_elastic_transcoder.types.video_parameters

        out["video"] = (
            aws_sdk_elastic_transcoder.types.video_parameters.deserialize_json(
                data["Video"]
            )
        )
    if "Thumbnails" in data:
        import aws_sdk_elastic_transcoder.types.thumbnails

        out["thumbnails"] = (
            aws_sdk_elastic_transcoder.types.thumbnails.deserialize_json(
                data["Thumbnails"]
            )
        )
    if "Type" in data:
        out["type"] = data["Type"]
    return out
