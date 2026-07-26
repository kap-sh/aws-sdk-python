"""Generated from Smithy shape ``com.amazonaws.rekognition#StartTextDetectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rekognition.types.client_request_token
    import capo_rekognition.types.job_tag
    import capo_rekognition.types.notification_channel
    import capo_rekognition.types.start_text_detection_filters
    import capo_rekognition.types.video


class StartTextDetectionRequest(TypedDict, closed=True):
    video: "capo_rekognition.types.video.Video"
    client_request_token: NotRequired[
        "capo_rekognition.types.client_request_token.ClientRequestToken"
    ]
    """<p>Idempotent token used to identify the start request. If you use the same token with multiple <code>StartTextDetection</code> requests, the same <code>JobId</code> is returned. Use <code>ClientRequestToken</code> to prevent the same job from being accidentaly started more than once.</p>"""
    notification_channel: NotRequired[
        "capo_rekognition.types.notification_channel.NotificationChannel"
    ]
    job_tag: NotRequired["capo_rekognition.types.job_tag.JobTag"]
    """<p>An identifier returned in the completion status published by your Amazon Simple Notification Service topic. For example, you can use <code>JobTag</code> to group related jobs and identify them in the completion notification.</p>"""
    filters: NotRequired[
        "capo_rekognition.types.start_text_detection_filters.StartTextDetectionFilters"
    ]
    """<p>Optional parameters that let you set criteria the text must meet to be included in your response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartTextDetectionRequest) -> dict:
    out: dict = {}
    import capo_rekognition.types.video

    out["Video"] = capo_rekognition.types.video.serialize_aws_json_1_1(value["video"])
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
    if "filters" in value:
        import capo_rekognition.types.start_text_detection_filters

        out["Filters"] = (
            capo_rekognition.types.start_text_detection_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartTextDetectionRequest:
    out: StartTextDetectionRequest = {}  # type: ignore[typeddict-item]
    if "Video" in data:
        import capo_rekognition.types.video

        out["video"] = capo_rekognition.types.video.deserialize_aws_json_1_1(
            data["Video"]
        )
    else:
        raise DeserializationError("StartTextDetectionRequest.video required")
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
    if "Filters" in data:
        import capo_rekognition.types.start_text_detection_filters

        out["filters"] = (
            capo_rekognition.types.start_text_detection_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    return out
