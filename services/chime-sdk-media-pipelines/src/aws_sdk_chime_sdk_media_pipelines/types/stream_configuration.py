"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#StreamConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.fragment_number_string
    import aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_arn
    import aws_sdk_chime_sdk_media_pipelines.types.stream_channel_definition


class StreamConfiguration(TypedDict):
    stream_arn: "aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_arn.KinesisVideoStreamArn"
    """<p>The ARN of the stream.</p>"""
    fragment_number: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.fragment_number_string.FragmentNumberString"
    ]
    """<p>The unique identifier of the fragment to begin processing.</p>"""
    stream_channel_definition: "aws_sdk_chime_sdk_media_pipelines.types.stream_channel_definition.StreamChannelDefinition"
    """<p>The streaming channel definition in the stream configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamConfiguration) -> dict:
    out: dict = {}
    out["StreamArn"] = value["stream_arn"]
    if "fragment_number" in value:
        out["FragmentNumber"] = value["fragment_number"]
    import aws_sdk_chime_sdk_media_pipelines.types.stream_channel_definition

    out["StreamChannelDefinition"] = (
        aws_sdk_chime_sdk_media_pipelines.types.stream_channel_definition.serialize_json(
            value["stream_channel_definition"]
        )
    )
    return out


def deserialize_json(data: dict) -> StreamConfiguration:
    out: StreamConfiguration = {}  # type: ignore[typeddict-item]
    if "StreamArn" in data:
        out["stream_arn"] = data["StreamArn"]
    else:
        raise DeserializationError("StreamConfiguration.stream_arn required")
    if "FragmentNumber" in data:
        out["fragment_number"] = data["FragmentNumber"]
    if "StreamChannelDefinition" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.stream_channel_definition

        out["stream_channel_definition"] = (
            aws_sdk_chime_sdk_media_pipelines.types.stream_channel_definition.deserialize_json(
                data["StreamChannelDefinition"]
            )
        )
    else:
        raise DeserializationError(
            "StreamConfiguration.stream_channel_definition required"
        )
    return out
