"""Generated from Smithy shape ``com.amazonaws.rekognition#StartSegmentDetectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.client_request_token
    import aws_sdk_rekognition.types.job_tag
    import aws_sdk_rekognition.types.notification_channel
    import aws_sdk_rekognition.types.segment_types
    import aws_sdk_rekognition.types.start_segment_detection_filters
    import aws_sdk_rekognition.types.video


class StartSegmentDetectionRequest(TypedDict):
    video: "aws_sdk_rekognition.types.video.Video"
    client_request_token: NotRequired[
        "aws_sdk_rekognition.types.client_request_token.ClientRequestToken"
    ]
    """<p>Idempotent token used to identify the start request. If you use the same token with multiple <code>StartSegmentDetection</code> requests, the same <code>JobId</code> is returned. Use <code>ClientRequestToken</code> to prevent the same job from being accidently started more than once. </p>"""
    notification_channel: NotRequired[
        "aws_sdk_rekognition.types.notification_channel.NotificationChannel"
    ]
    """<p>The ARN of the Amazon SNS topic to which you want Amazon Rekognition Video to publish the completion status of the segment detection operation. Note that the Amazon SNS topic must have a topic name that begins with <i>AmazonRekognition</i> if you are using the AmazonRekognitionServiceRole permissions policy to access the topic.</p>"""
    job_tag: NotRequired["aws_sdk_rekognition.types.job_tag.JobTag"]
    """<p>An identifier you specify that's returned in the completion notification that's published to your Amazon Simple Notification Service topic. For example, you can use <code>JobTag</code> to group related jobs and identify them in the completion notification.</p>"""
    filters: NotRequired[
        "aws_sdk_rekognition.types.start_segment_detection_filters.StartSegmentDetectionFilters"
    ]
    """<p>Filters for technical cue or shot detection.</p>"""
    segment_types: "aws_sdk_rekognition.types.segment_types.SegmentTypes"
    """<p>An array of segment types to detect in the video. Valid values are TECHNICAL_CUE and SHOT.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartSegmentDetectionRequest) -> dict:
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
    if "filters" in value:
        import aws_sdk_rekognition.types.start_segment_detection_filters

        out["Filters"] = (
            aws_sdk_rekognition.types.start_segment_detection_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    import aws_sdk_rekognition.types.segment_types

    out["SegmentTypes"] = (
        aws_sdk_rekognition.types.segment_types.serialize_aws_json_1_1(
            value["segment_types"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartSegmentDetectionRequest:
    out: StartSegmentDetectionRequest = {}  # type: ignore[typeddict-item]
    if "Video" in data:
        import aws_sdk_rekognition.types.video

        out["video"] = aws_sdk_rekognition.types.video.deserialize_aws_json_1_1(
            data["Video"]
        )
    else:
        raise DeserializationError("StartSegmentDetectionRequest.video required")
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
    if "Filters" in data:
        import aws_sdk_rekognition.types.start_segment_detection_filters

        out["filters"] = (
            aws_sdk_rekognition.types.start_segment_detection_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "SegmentTypes" in data:
        import aws_sdk_rekognition.types.segment_types

        out["segment_types"] = (
            aws_sdk_rekognition.types.segment_types.deserialize_aws_json_1_1(
                data["SegmentTypes"]
            )
        )
    else:
        raise DeserializationError(
            "StartSegmentDetectionRequest.segment_types required"
        )
    return out
