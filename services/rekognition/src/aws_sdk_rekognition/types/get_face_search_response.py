"""Generated from Smithy shape ``com.amazonaws.rekognition#GetFaceSearchResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.job_id
    import aws_sdk_rekognition.types.job_tag
    import aws_sdk_rekognition.types.pagination_token
    import aws_sdk_rekognition.types.person_matches
    import aws_sdk_rekognition.types.status_message
    import aws_sdk_rekognition.types.video
    import aws_sdk_rekognition.types.video_job_status
    import aws_sdk_rekognition.types.video_metadata


class GetFaceSearchResponse(TypedDict, closed=True):
    job_status: NotRequired["aws_sdk_rekognition.types.video_job_status.VideoJobStatus"]
    """<p>The current status of the face search job.</p>"""
    status_message: NotRequired[
        "aws_sdk_rekognition.types.status_message.StatusMessage"
    ]
    """<p>If the job fails, <code>StatusMessage</code> provides a descriptive error message.</p>"""
    next_token: NotRequired[
        "aws_sdk_rekognition.types.pagination_token.PaginationToken"
    ]
    """<p>If the response is truncated, Amazon Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of search results. </p>"""
    video_metadata: NotRequired[
        "aws_sdk_rekognition.types.video_metadata.VideoMetadata"
    ]
    """<p>Information about a video that Amazon Rekognition analyzed. <code>Videometadata</code> is returned in every page of paginated responses from a Amazon Rekognition Video operation. </p>"""
    persons: NotRequired["aws_sdk_rekognition.types.person_matches.PersonMatches"]
    """<p>An array of persons, <a>PersonMatch</a>, in the video whose face(s) match the face(s) in an Amazon Rekognition collection. It also includes time information for when persons are matched in the video. You specify the input collection in an initial call to <code>StartFaceSearch</code>. Each <code>Persons</code> element includes a time the person was matched, face match details (<code>FaceMatches</code>) for matching faces in the collection, and person information (<code>Person</code>) for the matched person. </p>"""
    job_id: NotRequired["aws_sdk_rekognition.types.job_id.JobId"]
    """<p>Job identifier for the face search operation for which you want to obtain results. The job identifer is returned by an initial call to StartFaceSearch.</p>"""
    video: NotRequired["aws_sdk_rekognition.types.video.Video"]
    job_tag: NotRequired["aws_sdk_rekognition.types.job_tag.JobTag"]
    """<p>A job identifier specified in the call to StartFaceSearch and returned in the job completion notification sent to your Amazon Simple Notification Service topic.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetFaceSearchResponse) -> dict:
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
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "video_metadata" in value:
        import aws_sdk_rekognition.types.video_metadata

        out["VideoMetadata"] = (
            aws_sdk_rekognition.types.video_metadata.serialize_aws_json_1_1(
                value["video_metadata"]
            )
        )
    if "persons" in value:
        import aws_sdk_rekognition.types.person_matches

        out["Persons"] = (
            aws_sdk_rekognition.types.person_matches.serialize_aws_json_1_1(
                value["persons"]
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


def deserialize_aws_json_1_1(data: dict) -> GetFaceSearchResponse:
    out: GetFaceSearchResponse = {}  # type: ignore[typeddict-item]
    if "JobStatus" in data:
        import aws_sdk_rekognition.types.video_job_status

        out["job_status"] = (
            aws_sdk_rekognition.types.video_job_status.deserialize_aws_json_1_1(
                data["JobStatus"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "VideoMetadata" in data:
        import aws_sdk_rekognition.types.video_metadata

        out["video_metadata"] = (
            aws_sdk_rekognition.types.video_metadata.deserialize_aws_json_1_1(
                data["VideoMetadata"]
            )
        )
    if "Persons" in data:
        import aws_sdk_rekognition.types.person_matches

        out["persons"] = (
            aws_sdk_rekognition.types.person_matches.deserialize_aws_json_1_1(
                data["Persons"]
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
