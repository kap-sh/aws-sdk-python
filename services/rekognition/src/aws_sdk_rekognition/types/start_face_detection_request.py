"""Generated from Smithy shape ``com.amazonaws.rekognition#StartFaceDetectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.client_request_token
    import aws_sdk_rekognition.types.face_attributes
    import aws_sdk_rekognition.types.job_tag
    import aws_sdk_rekognition.types.notification_channel
    import aws_sdk_rekognition.types.video


class StartFaceDetectionRequest(TypedDict, closed=True):
    video: "aws_sdk_rekognition.types.video.Video"
    """<p>The video in which you want to detect faces. The video must be stored in an Amazon S3 bucket.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_rekognition.types.client_request_token.ClientRequestToken"
    ]
    """<p>Idempotent token used to identify the start request. If you use the same token with multiple <code>StartFaceDetection</code> requests, the same <code>JobId</code> is returned. Use <code>ClientRequestToken</code> to prevent the same job from being accidently started more than once. </p>"""
    notification_channel: NotRequired[
        "aws_sdk_rekognition.types.notification_channel.NotificationChannel"
    ]
    """<p>The ARN of the Amazon SNS topic to which you want Amazon Rekognition Video to publish the completion status of the face detection operation. The Amazon SNS topic must have a topic name that begins with <i>AmazonRekognition</i> if you are using the AmazonRekognitionServiceRole permissions policy.</p>"""
    face_attributes: NotRequired[
        "aws_sdk_rekognition.types.face_attributes.FaceAttributes"
    ]
    """<p>The face attributes you want returned.</p> <p> <code>DEFAULT</code> - The following subset of facial attributes are returned: BoundingBox, Confidence, Pose, Quality and Landmarks. </p> <p> <code>ALL</code> - All facial attributes are returned.</p>"""
    job_tag: NotRequired["aws_sdk_rekognition.types.job_tag.JobTag"]
    """<p>An identifier you specify that's returned in the completion notification that's published to your Amazon Simple Notification Service topic. For example, you can use <code>JobTag</code> to group related jobs and identify them in the completion notification.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartFaceDetectionRequest) -> dict:
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
    if "face_attributes" in value:
        import aws_sdk_rekognition.types.face_attributes

        out["FaceAttributes"] = (
            aws_sdk_rekognition.types.face_attributes.serialize_aws_json_1_1(
                value["face_attributes"]
            )
        )
    if "job_tag" in value:
        out["JobTag"] = value["job_tag"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartFaceDetectionRequest:
    out: StartFaceDetectionRequest = {}  # type: ignore[typeddict-item]
    if "Video" in data:
        import aws_sdk_rekognition.types.video

        out["video"] = aws_sdk_rekognition.types.video.deserialize_aws_json_1_1(
            data["Video"]
        )
    else:
        raise DeserializationError("StartFaceDetectionRequest.video required")
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "NotificationChannel" in data:
        import aws_sdk_rekognition.types.notification_channel

        out["notification_channel"] = (
            aws_sdk_rekognition.types.notification_channel.deserialize_aws_json_1_1(
                data["NotificationChannel"]
            )
        )
    if "FaceAttributes" in data:
        import aws_sdk_rekognition.types.face_attributes

        out["face_attributes"] = (
            aws_sdk_rekognition.types.face_attributes.deserialize_aws_json_1_1(
                data["FaceAttributes"]
            )
        )
    if "JobTag" in data:
        out["job_tag"] = data["JobTag"]
    return out
