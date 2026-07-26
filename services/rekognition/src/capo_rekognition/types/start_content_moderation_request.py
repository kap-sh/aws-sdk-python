"""Generated from Smithy shape ``com.amazonaws.rekognition#StartContentModerationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rekognition.types.client_request_token
    import capo_rekognition.types.job_tag
    import capo_rekognition.types.notification_channel
    import capo_rekognition.types.percent
    import capo_rekognition.types.video


class StartContentModerationRequest(TypedDict, closed=True):
    video: "capo_rekognition.types.video.Video"
    """<p>The video in which you want to detect inappropriate, unwanted, or offensive content. The video must be stored in an Amazon S3 bucket.</p>"""
    min_confidence: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>Specifies the minimum confidence that Amazon Rekognition must have in order to return a moderated content label. Confidence represents how certain Amazon Rekognition is that the moderated content is correctly identified. 0 is the lowest confidence. 100 is the highest confidence. Amazon Rekognition doesn't return any moderated content labels with a confidence level lower than this specified value. If you don't specify <code>MinConfidence</code>, <code>GetContentModeration</code> returns labels with confidence values greater than or equal to 50 percent.</p>"""
    client_request_token: NotRequired[
        "capo_rekognition.types.client_request_token.ClientRequestToken"
    ]
    """<p>Idempotent token used to identify the start request. If you use the same token with multiple <code>StartContentModeration</code> requests, the same <code>JobId</code> is returned. Use <code>ClientRequestToken</code> to prevent the same job from being accidently started more than once. </p>"""
    notification_channel: NotRequired[
        "capo_rekognition.types.notification_channel.NotificationChannel"
    ]
    """<p>The Amazon SNS topic ARN that you want Amazon Rekognition Video to publish the completion status of the content analysis to. The Amazon SNS topic must have a topic name that begins with <i>AmazonRekognition</i> if you are using the AmazonRekognitionServiceRole permissions policy to access the topic.</p>"""
    job_tag: NotRequired["capo_rekognition.types.job_tag.JobTag"]
    """<p>An identifier you specify that's returned in the completion notification that's published to your Amazon Simple Notification Service topic. For example, you can use <code>JobTag</code> to group related jobs and identify them in the completion notification.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartContentModerationRequest) -> dict:
    out: dict = {}
    import capo_rekognition.types.video

    out["Video"] = capo_rekognition.types.video.serialize_aws_json_1_1(value["video"])
    if "min_confidence" in value:
        out["MinConfidence"] = value["min_confidence"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "notification_channel" in value:
        import capo_rekognition.types.notification_channel

        out["NotificationChannel"] = (
            capo_rekognition.types.notification_channel.serialize_aws_json_1_1(
                value["notification_channel"]
            )
        )
    if "job_tag" in value:
        out["JobTag"] = value["job_tag"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartContentModerationRequest:
    out: StartContentModerationRequest = {}  # type: ignore[typeddict-item]
    if "Video" in data:
        import capo_rekognition.types.video

        out["video"] = capo_rekognition.types.video.deserialize_aws_json_1_1(
            data["Video"]
        )
    else:
        raise DeserializationError("StartContentModerationRequest.video required")
    if "MinConfidence" in data:
        out["min_confidence"] = data["MinConfidence"]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "NotificationChannel" in data:
        import capo_rekognition.types.notification_channel

        out["notification_channel"] = (
            capo_rekognition.types.notification_channel.deserialize_aws_json_1_1(
                data["NotificationChannel"]
            )
        )
    if "JobTag" in data:
        out["job_tag"] = data["JobTag"]
    return out
