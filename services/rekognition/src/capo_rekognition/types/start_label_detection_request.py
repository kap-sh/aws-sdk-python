"""Generated from Smithy shape ``com.amazonaws.rekognition#StartLabelDetectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rekognition.types.client_request_token
    import capo_rekognition.types.job_tag
    import capo_rekognition.types.label_detection_feature_list
    import capo_rekognition.types.label_detection_settings
    import capo_rekognition.types.notification_channel
    import capo_rekognition.types.percent
    import capo_rekognition.types.video


class StartLabelDetectionRequest(TypedDict, closed=True):
    video: "capo_rekognition.types.video.Video"
    """<p>The video in which you want to detect labels. The video must be stored in an Amazon S3 bucket.</p>"""
    client_request_token: NotRequired[
        "capo_rekognition.types.client_request_token.ClientRequestToken"
    ]
    """<p>Idempotent token used to identify the start request. If you use the same token with multiple <code>StartLabelDetection</code> requests, the same <code>JobId</code> is returned. Use <code>ClientRequestToken</code> to prevent the same job from being accidently started more than once. </p>"""
    min_confidence: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>Specifies the minimum confidence that Amazon Rekognition Video must have in order to return a detected label. Confidence represents how certain Amazon Rekognition is that a label is correctly identified.0 is the lowest confidence. 100 is the highest confidence. Amazon Rekognition Video doesn't return any labels with a confidence level lower than this specified value.</p> <p>If you don't specify <code>MinConfidence</code>, the operation returns labels and bounding boxes (if detected) with confidence values greater than or equal to 50 percent.</p>"""
    notification_channel: NotRequired[
        "capo_rekognition.types.notification_channel.NotificationChannel"
    ]
    """<p>The Amazon SNS topic ARN you want Amazon Rekognition Video to publish the completion status of the label detection operation to. The Amazon SNS topic must have a topic name that begins with <i>AmazonRekognition</i> if you are using the AmazonRekognitionServiceRole permissions policy.</p>"""
    job_tag: NotRequired["capo_rekognition.types.job_tag.JobTag"]
    """<p>An identifier you specify that's returned in the completion notification that's published to your Amazon Simple Notification Service topic. For example, you can use <code>JobTag</code> to group related jobs and identify them in the completion notification.</p>"""
    features: NotRequired[
        "capo_rekognition.types.label_detection_feature_list.LabelDetectionFeatureList"
    ]
    """<p>The features to return after video analysis. You can specify that GENERAL_LABELS are returned.</p>"""
    settings: NotRequired[
        "capo_rekognition.types.label_detection_settings.LabelDetectionSettings"
    ]
    """<p>The settings for a StartLabelDetection request.Contains the specified parameters for the label detection request of an asynchronous label analysis operation. Settings can include filters for GENERAL_LABELS.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartLabelDetectionRequest) -> dict:
    out: dict = {}
    import capo_rekognition.types.video

    out["Video"] = capo_rekognition.types.video.serialize_aws_json_1_1(value["video"])
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "min_confidence" in value:
        out["MinConfidence"] = value["min_confidence"]
    if "notification_channel" in value:
        import capo_rekognition.types.notification_channel

        out["NotificationChannel"] = (
            capo_rekognition.types.notification_channel.serialize_aws_json_1_1(
                value["notification_channel"]
            )
        )
    if "job_tag" in value:
        out["JobTag"] = value["job_tag"]
    if "features" in value:
        import capo_rekognition.types.label_detection_feature_list

        out["Features"] = (
            capo_rekognition.types.label_detection_feature_list.serialize_aws_json_1_1(
                value["features"]
            )
        )
    if "settings" in value:
        import capo_rekognition.types.label_detection_settings

        out["Settings"] = (
            capo_rekognition.types.label_detection_settings.serialize_aws_json_1_1(
                value["settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartLabelDetectionRequest:
    out: StartLabelDetectionRequest = {}  # type: ignore[typeddict-item]
    if "Video" in data:
        import capo_rekognition.types.video

        out["video"] = capo_rekognition.types.video.deserialize_aws_json_1_1(
            data["Video"]
        )
    else:
        raise DeserializationError("StartLabelDetectionRequest.video required")
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "MinConfidence" in data:
        out["min_confidence"] = data["MinConfidence"]
    if "NotificationChannel" in data:
        import capo_rekognition.types.notification_channel

        out["notification_channel"] = (
            capo_rekognition.types.notification_channel.deserialize_aws_json_1_1(
                data["NotificationChannel"]
            )
        )
    if "JobTag" in data:
        out["job_tag"] = data["JobTag"]
    if "Features" in data:
        import capo_rekognition.types.label_detection_feature_list

        out["features"] = (
            capo_rekognition.types.label_detection_feature_list.deserialize_aws_json_1_1(
                data["Features"]
            )
        )
    if "Settings" in data:
        import capo_rekognition.types.label_detection_settings

        out["settings"] = (
            capo_rekognition.types.label_detection_settings.deserialize_aws_json_1_1(
                data["Settings"]
            )
        )
    return out
