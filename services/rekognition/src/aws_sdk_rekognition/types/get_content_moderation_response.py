"""Generated from Smithy shape ``com.amazonaws.rekognition#GetContentModerationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.content_moderation_detections
    import aws_sdk_rekognition.types.get_content_moderation_request_metadata
    import aws_sdk_rekognition.types.job_id
    import aws_sdk_rekognition.types.job_tag
    import aws_sdk_rekognition.types.pagination_token
    import aws_sdk_rekognition.types.status_message
    import aws_sdk_rekognition.types.string
    import aws_sdk_rekognition.types.video
    import aws_sdk_rekognition.types.video_job_status
    import aws_sdk_rekognition.types.video_metadata


class GetContentModerationResponse(TypedDict):
    job_status: NotRequired["aws_sdk_rekognition.types.video_job_status.VideoJobStatus"]
    """<p>The current status of the content moderation analysis job.</p>"""
    status_message: NotRequired[
        "aws_sdk_rekognition.types.status_message.StatusMessage"
    ]
    """<p>If the job fails, <code>StatusMessage</code> provides a descriptive error message.</p>"""
    video_metadata: NotRequired[
        "aws_sdk_rekognition.types.video_metadata.VideoMetadata"
    ]
    """<p>Information about a video that Amazon Rekognition analyzed. <code>Videometadata</code> is returned in every page of paginated responses from <code>GetContentModeration</code>. </p>"""
    moderation_labels: NotRequired[
        "aws_sdk_rekognition.types.content_moderation_detections.ContentModerationDetections"
    ]
    """<p>The detected inappropriate, unwanted, or offensive content moderation labels and the time(s) they were detected.</p>"""
    next_token: NotRequired[
        "aws_sdk_rekognition.types.pagination_token.PaginationToken"
    ]
    """<p>If the response is truncated, Amazon Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of content moderation labels. </p>"""
    moderation_model_version: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>Version number of the moderation detection model that was used to detect inappropriate, unwanted, or offensive content.</p>"""
    job_id: NotRequired["aws_sdk_rekognition.types.job_id.JobId"]
    """<p>Job identifier for the content moderation operation for which you want to obtain results. The job identifer is returned by an initial call to StartContentModeration.</p>"""
    video: NotRequired["aws_sdk_rekognition.types.video.Video"]
    job_tag: NotRequired["aws_sdk_rekognition.types.job_tag.JobTag"]
    """<p>A job identifier specified in the call to StartContentModeration and returned in the job completion notification sent to your Amazon Simple Notification Service topic.</p>"""
    get_request_metadata: NotRequired[
        "aws_sdk_rekognition.types.get_content_moderation_request_metadata.GetContentModerationRequestMetadata"
    ]
    """<p>Information about the paramters used when getting a response. Includes information on aggregation and sorting methods.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContentModerationResponse) -> dict:
    out: dict = {}
    if "job_status" in value:
        import aws_sdk_rekognition.types.video_job_status

        out["JobStatus"] = (
            aws_sdk_rekognition.types.video_job_status.serialize_aws_json_1_1(
                value["job_status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "video_metadata" in value:
        import aws_sdk_rekognition.types.video_metadata

        out["VideoMetadata"] = (
            aws_sdk_rekognition.types.video_metadata.serialize_aws_json_1_1(
                value["video_metadata"]
            )
        )
    if "moderation_labels" in value:
        import aws_sdk_rekognition.types.content_moderation_detections

        out["ModerationLabels"] = (
            aws_sdk_rekognition.types.content_moderation_detections.serialize_aws_json_1_1(
                value["moderation_labels"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "moderation_model_version" in value:
        out["ModerationModelVersion"] = value["moderation_model_version"]
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "video" in value:
        import aws_sdk_rekognition.types.video

        out["Video"] = aws_sdk_rekognition.types.video.serialize_aws_json_1_1(
            value["video"]
        )
    if "job_tag" in value:
        out["JobTag"] = value["job_tag"]
    if "get_request_metadata" in value:
        import aws_sdk_rekognition.types.get_content_moderation_request_metadata

        out["GetRequestMetadata"] = (
            aws_sdk_rekognition.types.get_content_moderation_request_metadata.serialize_aws_json_1_1(
                value["get_request_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContentModerationResponse:
    out: GetContentModerationResponse = {}  # type: ignore[typeddict-item]
    if "JobStatus" in data:
        import aws_sdk_rekognition.types.video_job_status

        out["job_status"] = (
            aws_sdk_rekognition.types.video_job_status.deserialize_aws_json_1_1(
                data["JobStatus"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "VideoMetadata" in data:
        import aws_sdk_rekognition.types.video_metadata

        out["video_metadata"] = (
            aws_sdk_rekognition.types.video_metadata.deserialize_aws_json_1_1(
                data["VideoMetadata"]
            )
        )
    if "ModerationLabels" in data:
        import aws_sdk_rekognition.types.content_moderation_detections

        out["moderation_labels"] = (
            aws_sdk_rekognition.types.content_moderation_detections.deserialize_aws_json_1_1(
                data["ModerationLabels"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ModerationModelVersion" in data:
        out["moderation_model_version"] = data["ModerationModelVersion"]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    if "Video" in data:
        import aws_sdk_rekognition.types.video

        out["video"] = aws_sdk_rekognition.types.video.deserialize_aws_json_1_1(
            data["Video"]
        )
    if "JobTag" in data:
        out["job_tag"] = data["JobTag"]
    if "GetRequestMetadata" in data:
        import aws_sdk_rekognition.types.get_content_moderation_request_metadata

        out["get_request_metadata"] = (
            aws_sdk_rekognition.types.get_content_moderation_request_metadata.deserialize_aws_json_1_1(
                data["GetRequestMetadata"]
            )
        )
    return out
