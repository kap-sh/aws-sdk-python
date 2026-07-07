"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#StartSpeakerSearchTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.arn
    import aws_sdk_chime_sdk_media_pipelines.types.client_request_token
    import aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_source_task_configuration
    import aws_sdk_chime_sdk_media_pipelines.types.non_empty_string


class StartSpeakerSearchTaskRequest(TypedDict, closed=True):
    identifier: (
        "aws_sdk_chime_sdk_media_pipelines.types.non_empty_string.NonEmptyString"
    )
    """<p>The unique identifier of the resource to be updated. Valid values include the ID and ARN of the media insights pipeline.</p>"""
    voice_profile_domain_arn: "aws_sdk_chime_sdk_media_pipelines.types.arn.Arn"
    """<p>The ARN of the voice profile domain that will store the voice profile.</p>"""
    kinesis_video_stream_source_task_configuration: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_source_task_configuration.KinesisVideoStreamSourceTaskConfiguration"
    ]
    """<p>The task configuration for the Kinesis video stream source of the media insights pipeline.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.client_request_token.ClientRequestToken"
    ]
    """<p>The unique identifier for the client request. Use a different token for different speaker search tasks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSpeakerSearchTaskRequest) -> dict:
    out: dict = {}
    out["VoiceProfileDomainArn"] = value["voice_profile_domain_arn"]
    if "kinesis_video_stream_source_task_configuration" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_source_task_configuration

        out["KinesisVideoStreamSourceTaskConfiguration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_source_task_configuration.serialize_json(
                value["kinesis_video_stream_source_task_configuration"]
            )
        )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> StartSpeakerSearchTaskRequest:
    out: StartSpeakerSearchTaskRequest = {}  # type: ignore[typeddict-item]
    if "VoiceProfileDomainArn" in data:
        out["voice_profile_domain_arn"] = data["VoiceProfileDomainArn"]
    else:
        raise DeserializationError(
            "StartSpeakerSearchTaskRequest.voice_profile_domain_arn required"
        )
    if "KinesisVideoStreamSourceTaskConfiguration" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_source_task_configuration

        out["kinesis_video_stream_source_task_configuration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_source_task_configuration.deserialize_json(
                data["KinesisVideoStreamSourceTaskConfiguration"]
            )
        )
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
