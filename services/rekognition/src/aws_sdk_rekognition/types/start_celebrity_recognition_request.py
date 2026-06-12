"""Generated from Smithy shape ``com.amazonaws.rekognition#StartCelebrityRecognitionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.client_request_token
    import aws_sdk_rekognition.types.job_tag
    import aws_sdk_rekognition.types.notification_channel
    import aws_sdk_rekognition.types.video


class StartCelebrityRecognitionRequest(TypedDict):
    video: "aws_sdk_rekognition.types.video.Video"
    """<p>The video in which you want to recognize celebrities. The video must be stored in an Amazon S3 bucket.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_rekognition.types.client_request_token.ClientRequestToken"
    ]
    """<p>Idempotent token used to identify the start request. If you use the same token with multiple <code>StartCelebrityRecognition</code> requests, the same <code>JobId</code> is returned. Use <code>ClientRequestToken</code> to prevent the same job from being accidently started more than once. </p>"""
    notification_channel: NotRequired[
        "aws_sdk_rekognition.types.notification_channel.NotificationChannel"
    ]
    """<p>The Amazon SNS topic ARN that you want Amazon Rekognition Video to publish the completion status of the celebrity recognition analysis to. The Amazon SNS topic must have a topic name that begins with <i>AmazonRekognition</i> if you are using the AmazonRekognitionServiceRole permissions policy.</p>"""
    job_tag: NotRequired["aws_sdk_rekognition.types.job_tag.JobTag"]
    """<p>An identifier you specify that's returned in the completion notification that's published to your Amazon Simple Notification Service topic. For example, you can use <code>JobTag</code> to group related jobs and identify them in the completion notification.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartCelebrityRecognitionRequest) -> dict:
    out: dict = {}
    import aws_sdk_rekognition.types.video

    out["Video"] = aws_sdk_rekognition.types.video.serialize_aws_json_1_1(
        value["video"]
    )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "notification_channel" in value:
        import aws_sdk_rekognition.types.notification_channel

        out["NotificationChannel"] = (
            aws_sdk_rekognition.types.notification_channel.serialize_aws_json_1_1(
                value["notification_channel"]
            )
        )
    if "job_tag" in value:
        out["JobTag"] = value["job_tag"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartCelebrityRecognitionRequest:
    out: StartCelebrityRecognitionRequest = {}  # type: ignore[typeddict-item]
    if "Video" in data:
        import aws_sdk_rekognition.types.video

        out["video"] = aws_sdk_rekognition.types.video.deserialize_aws_json_1_1(
            data["Video"]
        )
    else:
        raise DeserializationError("StartCelebrityRecognitionRequest.video required")
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "NotificationChannel" in data:
        import aws_sdk_rekognition.types.notification_channel

        out["notification_channel"] = (
            aws_sdk_rekognition.types.notification_channel.deserialize_aws_json_1_1(
                data["NotificationChannel"]
            )
        )
    if "JobTag" in data:
        out["job_tag"] = data["JobTag"]
    return out
