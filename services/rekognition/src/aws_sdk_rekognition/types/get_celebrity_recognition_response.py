"""Generated from Smithy shape ``com.amazonaws.rekognition#GetCelebrityRecognitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.celebrity_recognitions
    import aws_sdk_rekognition.types.job_id
    import aws_sdk_rekognition.types.job_tag
    import aws_sdk_rekognition.types.pagination_token
    import aws_sdk_rekognition.types.status_message
    import aws_sdk_rekognition.types.video
    import aws_sdk_rekognition.types.video_job_status
    import aws_sdk_rekognition.types.video_metadata


class GetCelebrityRecognitionResponse(TypedDict, closed=True):
    job_status: NotRequired["aws_sdk_rekognition.types.video_job_status.VideoJobStatus"]
    """<p>The current status of the celebrity recognition job.</p>"""
    status_message: NotRequired[
        "aws_sdk_rekognition.types.status_message.StatusMessage"
    ]
    """<p>If the job fails, <code>StatusMessage</code> provides a descriptive error message.</p>"""
    video_metadata: NotRequired[
        "aws_sdk_rekognition.types.video_metadata.VideoMetadata"
    ]
    """<p>Information about a video that Amazon Rekognition Video analyzed. <code>Videometadata</code> is returned in every page of paginated responses from a Amazon Rekognition Video operation.</p>"""
    next_token: NotRequired[
        "aws_sdk_rekognition.types.pagination_token.PaginationToken"
    ]
    """<p>If the response is truncated, Amazon Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of celebrities.</p>"""
    celebrities: NotRequired[
        "aws_sdk_rekognition.types.celebrity_recognitions.CelebrityRecognitions"
    ]
    """<p>Array of celebrities recognized in the video.</p>"""
    job_id: NotRequired["aws_sdk_rekognition.types.job_id.JobId"]
    """<p>Job identifier for the celebrity recognition operation for which you want to obtain results. The job identifer is returned by an initial call to StartCelebrityRecognition.</p>"""
    video: NotRequired["aws_sdk_rekognition.types.video.Video"]
    job_tag: NotRequired["aws_sdk_rekognition.types.job_tag.JobTag"]
    """<p>A job identifier specified in the call to StartCelebrityRecognition and returned in the job completion notification sent to your Amazon Simple Notification Service topic.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCelebrityRecognitionResponse) -> dict:
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
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "celebrities" in value:
        import aws_sdk_rekognition.types.celebrity_recognitions

        out["Celebrities"] = (
            aws_sdk_rekognition.types.celebrity_recognitions.serialize_aws_json_1_1(
                value["celebrities"]
            )
        )
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "video" in value:
        import aws_sdk_rekognition.types.video

        out["Video"] = aws_sdk_rekognition.types.video.serialize_aws_json_1_1(
            value["video"]
        )
    if "job_tag" in value:
        out["JobTag"] = value["job_tag"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCelebrityRecognitionResponse:
    out: GetCelebrityRecognitionResponse = {}  # type: ignore[typeddict-item]
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
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Celebrities" in data:
        import aws_sdk_rekognition.types.celebrity_recognitions

        out["celebrities"] = (
            aws_sdk_rekognition.types.celebrity_recognitions.deserialize_aws_json_1_1(
                data["Celebrities"]
            )
        )
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    if "Video" in data:
        import aws_sdk_rekognition.types.video

        out["video"] = aws_sdk_rekognition.types.video.deserialize_aws_json_1_1(
            data["Video"]
        )
    if "JobTag" in data:
        out["job_tag"] = data["JobTag"]
    return out
