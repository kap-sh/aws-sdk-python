"""Generated from Smithy shape ``com.amazonaws.rekognition#GetTextDetectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.job_id
    import capo_rekognition.types.job_tag
    import capo_rekognition.types.pagination_token
    import capo_rekognition.types.status_message
    import capo_rekognition.types.string
    import capo_rekognition.types.text_detection_results
    import capo_rekognition.types.video
    import capo_rekognition.types.video_job_status
    import capo_rekognition.types.video_metadata


class GetTextDetectionResponse(TypedDict, closed=True):
    job_status: NotRequired["capo_rekognition.types.video_job_status.VideoJobStatus"]
    """<p>Current status of the text detection job.</p>"""
    status_message: NotRequired["capo_rekognition.types.status_message.StatusMessage"]
    """<p>If the job fails, <code>StatusMessage</code> provides a descriptive error message.</p>"""
    video_metadata: NotRequired["capo_rekognition.types.video_metadata.VideoMetadata"]
    text_detections: NotRequired[
        "capo_rekognition.types.text_detection_results.TextDetectionResults"
    ]
    """<p>An array of text detected in the video. Each element contains the detected text, the time in milliseconds from the start of the video that the text was detected, and where it was detected on the screen.</p>"""
    next_token: NotRequired["capo_rekognition.types.pagination_token.PaginationToken"]
    """<p>If the response is truncated, Amazon Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of text.</p>"""
    text_model_version: NotRequired["capo_rekognition.types.string.String"]
    """<p>Version number of the text detection model that was used to detect text.</p>"""
    job_id: NotRequired["capo_rekognition.types.job_id.JobId"]
    """<p>Job identifier for the text detection operation for which you want to obtain results. The job identifer is returned by an initial call to StartTextDetection.</p>"""
    video: NotRequired["capo_rekognition.types.video.Video"]
    job_tag: NotRequired["capo_rekognition.types.job_tag.JobTag"]
    """<p>A job identifier specified in the call to StartTextDetection and returned in the job completion notification sent to your Amazon Simple Notification Service topic.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTextDetectionResponse) -> dict:
    out: dict = {}
    if "job_status" in value:
        import capo_rekognition.types.video_job_status

        out["JobStatus"] = (
            capo_rekognition.types.video_job_status.serialize_aws_json_1_1(
                value["job_status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "video_metadata" in value:
        import capo_rekognition.types.video_metadata

        out["VideoMetadata"] = (
            capo_rekognition.types.video_metadata.serialize_aws_json_1_1(
                value["video_metadata"]
            )
        )
    if "text_detections" in value:
        import capo_rekognition.types.text_detection_results

        out["TextDetections"] = (
            capo_rekognition.types.text_detection_results.serialize_aws_json_1_1(
                value["text_detections"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "text_model_version" in value:
        out["TextModelVersion"] = value["text_model_version"]
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "video" in value:
        import capo_rekognition.types.video

        out["Video"] = capo_rekognition.types.video.serialize_aws_json_1_1(
            value["video"]
        )
    if "job_tag" in value:
        out["JobTag"] = value["job_tag"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTextDetectionResponse:
    out: GetTextDetectionResponse = {}  # type: ignore[typeddict-item]
    if "JobStatus" in data:
        import capo_rekognition.types.video_job_status

        out["job_status"] = (
            capo_rekognition.types.video_job_status.deserialize_aws_json_1_1(
                data["JobStatus"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "VideoMetadata" in data:
        import capo_rekognition.types.video_metadata

        out["video_metadata"] = (
            capo_rekognition.types.video_metadata.deserialize_aws_json_1_1(
                data["VideoMetadata"]
            )
        )
    if "TextDetections" in data:
        import capo_rekognition.types.text_detection_results

        out["text_detections"] = (
            capo_rekognition.types.text_detection_results.deserialize_aws_json_1_1(
                data["TextDetections"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "TextModelVersion" in data:
        out["text_model_version"] = data["TextModelVersion"]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    if "Video" in data:
        import capo_rekognition.types.video

        out["video"] = capo_rekognition.types.video.deserialize_aws_json_1_1(
            data["Video"]
        )
    if "JobTag" in data:
        out["job_tag"] = data["JobTag"]
    return out
