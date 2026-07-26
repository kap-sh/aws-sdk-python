"""Generated from Smithy shape ``com.amazonaws.rekognition#GetLabelDetectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.get_label_detection_request_metadata
    import capo_rekognition.types.job_id
    import capo_rekognition.types.job_tag
    import capo_rekognition.types.label_detections
    import capo_rekognition.types.pagination_token
    import capo_rekognition.types.status_message
    import capo_rekognition.types.string
    import capo_rekognition.types.video
    import capo_rekognition.types.video_job_status
    import capo_rekognition.types.video_metadata


class GetLabelDetectionResponse(TypedDict, closed=True):
    job_status: NotRequired["capo_rekognition.types.video_job_status.VideoJobStatus"]
    """<p>The current status of the label detection job.</p>"""
    status_message: NotRequired["capo_rekognition.types.status_message.StatusMessage"]
    """<p>If the job fails, <code>StatusMessage</code> provides a descriptive error message.</p>"""
    video_metadata: NotRequired["capo_rekognition.types.video_metadata.VideoMetadata"]
    """<p>Information about a video that Amazon Rekognition Video analyzed. <code>Videometadata</code> is returned in every page of paginated responses from a Amazon Rekognition video operation.</p>"""
    next_token: NotRequired["capo_rekognition.types.pagination_token.PaginationToken"]
    """<p>If the response is truncated, Amazon Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of labels.</p>"""
    labels: NotRequired["capo_rekognition.types.label_detections.LabelDetections"]
    """<p>An array of labels detected in the video. Each element contains the detected label and the time, in milliseconds from the start of the video, that the label was detected. </p>"""
    label_model_version: NotRequired["capo_rekognition.types.string.String"]
    """<p>Version number of the label detection model that was used to detect labels.</p>"""
    job_id: NotRequired["capo_rekognition.types.job_id.JobId"]
    """<p>Job identifier for the label detection operation for which you want to obtain results. The job identifer is returned by an initial call to StartLabelDetection.</p>"""
    video: NotRequired["capo_rekognition.types.video.Video"]
    job_tag: NotRequired["capo_rekognition.types.job_tag.JobTag"]
    """<p>A job identifier specified in the call to StartLabelDetection and returned in the job completion notification sent to your Amazon Simple Notification Service topic.</p>"""
    get_request_metadata: NotRequired[
        "capo_rekognition.types.get_label_detection_request_metadata.GetLabelDetectionRequestMetadata"
    ]
    """<p>Information about the paramters used when getting a response. Includes information on aggregation and sorting methods.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLabelDetectionResponse) -> dict:
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
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "labels" in value:
        import capo_rekognition.types.label_detections

        out["Labels"] = capo_rekognition.types.label_detections.serialize_aws_json_1_1(
            value["labels"]
        )
    if "label_model_version" in value:
        out["LabelModelVersion"] = value["label_model_version"]
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "video" in value:
        import capo_rekognition.types.video

        out["Video"] = capo_rekognition.types.video.serialize_aws_json_1_1(
            value["video"]
        )
    if "job_tag" in value:
        out["JobTag"] = value["job_tag"]
    if "get_request_metadata" in value:
        import capo_rekognition.types.get_label_detection_request_metadata

        out["GetRequestMetadata"] = (
            capo_rekognition.types.get_label_detection_request_metadata.serialize_aws_json_1_1(
                value["get_request_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLabelDetectionResponse:
    out: GetLabelDetectionResponse = {}  # type: ignore[typeddict-item]
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
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Labels" in data:
        import capo_rekognition.types.label_detections

        out["labels"] = (
            capo_rekognition.types.label_detections.deserialize_aws_json_1_1(
                data["Labels"]
            )
        )
    if "LabelModelVersion" in data:
        out["label_model_version"] = data["LabelModelVersion"]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    if "Video" in data:
        import capo_rekognition.types.video

        out["video"] = capo_rekognition.types.video.deserialize_aws_json_1_1(
            data["Video"]
        )
    if "JobTag" in data:
        out["job_tag"] = data["JobTag"]
    if "GetRequestMetadata" in data:
        import capo_rekognition.types.get_label_detection_request_metadata

        out["get_request_metadata"] = (
            capo_rekognition.types.get_label_detection_request_metadata.deserialize_aws_json_1_1(
                data["GetRequestMetadata"]
            )
        )
    return out
