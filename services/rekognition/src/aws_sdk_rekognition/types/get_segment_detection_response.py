"""Generated from Smithy shape ``com.amazonaws.rekognition#GetSegmentDetectionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.audio_metadata_list
    import aws_sdk_rekognition.types.job_id
    import aws_sdk_rekognition.types.job_tag
    import aws_sdk_rekognition.types.pagination_token
    import aws_sdk_rekognition.types.segment_detections
    import aws_sdk_rekognition.types.segment_types_info
    import aws_sdk_rekognition.types.status_message
    import aws_sdk_rekognition.types.video
    import aws_sdk_rekognition.types.video_job_status
    import aws_sdk_rekognition.types.video_metadata_list


class GetSegmentDetectionResponse(TypedDict):
    job_status: NotRequired["aws_sdk_rekognition.types.video_job_status.VideoJobStatus"]
    """<p>Current status of the segment detection job.</p>"""
    status_message: NotRequired[
        "aws_sdk_rekognition.types.status_message.StatusMessage"
    ]
    """<p>If the job fails, <code>StatusMessage</code> provides a descriptive error message.</p>"""
    video_metadata: NotRequired[
        "aws_sdk_rekognition.types.video_metadata_list.VideoMetadataList"
    ]
    """<p>Currently, Amazon Rekognition Video returns a single object in the <code>VideoMetadata</code> array. The object contains information about the video stream in the input file that Amazon Rekognition Video chose to analyze. The <code>VideoMetadata</code> object includes the video codec, video format and other information. Video metadata is returned in each page of information returned by <code>GetSegmentDetection</code>.</p>"""
    audio_metadata: NotRequired[
        "aws_sdk_rekognition.types.audio_metadata_list.AudioMetadataList"
    ]
    """<p>An array of objects. There can be multiple audio streams. Each <code>AudioMetadata</code> object contains metadata for a single audio stream. Audio information in an <code>AudioMetadata</code> objects includes the audio codec, the number of audio channels, the duration of the audio stream, and the sample rate. Audio metadata is returned in each page of information returned by <code>GetSegmentDetection</code>.</p>"""
    next_token: NotRequired[
        "aws_sdk_rekognition.types.pagination_token.PaginationToken"
    ]
    """<p>If the previous response was incomplete (because there are more labels to retrieve), Amazon Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of text.</p>"""
    segments: NotRequired[
        "aws_sdk_rekognition.types.segment_detections.SegmentDetections"
    ]
    """<p>An array of segments detected in a video. The array is sorted by the segment types (TECHNICAL_CUE or SHOT) specified in the <code>SegmentTypes</code> input parameter of <code>StartSegmentDetection</code>. Within each segment type the array is sorted by timestamp values.</p>"""
    selected_segment_types: NotRequired[
        "aws_sdk_rekognition.types.segment_types_info.SegmentTypesInfo"
    ]
    """<p>An array containing the segment types requested in the call to <code>StartSegmentDetection</code>. </p>"""
    job_id: NotRequired["aws_sdk_rekognition.types.job_id.JobId"]
    """<p>Job identifier for the segment detection operation for which you want to obtain results. The job identifer is returned by an initial call to StartSegmentDetection.</p>"""
    video: NotRequired["aws_sdk_rekognition.types.video.Video"]
    job_tag: NotRequired["aws_sdk_rekognition.types.job_tag.JobTag"]
    """<p>A job identifier specified in the call to StartSegmentDetection and returned in the job completion notification sent to your Amazon Simple Notification Service topic.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSegmentDetectionResponse) -> dict:
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
        import aws_sdk_rekognition.types.video_metadata_list

        out["VideoMetadata"] = (
            aws_sdk_rekognition.types.video_metadata_list.serialize_aws_json_1_1(
                value["video_metadata"]
            )
        )
    if "audio_metadata" in value:
        import aws_sdk_rekognition.types.audio_metadata_list

        out["AudioMetadata"] = (
            aws_sdk_rekognition.types.audio_metadata_list.serialize_aws_json_1_1(
                value["audio_metadata"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "segments" in value:
        import aws_sdk_rekognition.types.segment_detections

        out["Segments"] = (
            aws_sdk_rekognition.types.segment_detections.serialize_aws_json_1_1(
                value["segments"]
            )
        )
    if "selected_segment_types" in value:
        import aws_sdk_rekognition.types.segment_types_info

        out["SelectedSegmentTypes"] = (
            aws_sdk_rekognition.types.segment_types_info.serialize_aws_json_1_1(
                value["selected_segment_types"]
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


def deserialize_aws_json_1_1(data: dict) -> GetSegmentDetectionResponse:
    out: GetSegmentDetectionResponse = {}  # type: ignore[typeddict-item]
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
        import aws_sdk_rekognition.types.video_metadata_list

        out["video_metadata"] = (
            aws_sdk_rekognition.types.video_metadata_list.deserialize_aws_json_1_1(
                data["VideoMetadata"]
            )
        )
    if "AudioMetadata" in data:
        import aws_sdk_rekognition.types.audio_metadata_list

        out["audio_metadata"] = (
            aws_sdk_rekognition.types.audio_metadata_list.deserialize_aws_json_1_1(
                data["AudioMetadata"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Segments" in data:
        import aws_sdk_rekognition.types.segment_detections

        out["segments"] = (
            aws_sdk_rekognition.types.segment_detections.deserialize_aws_json_1_1(
                data["Segments"]
            )
        )
    if "SelectedSegmentTypes" in data:
        import aws_sdk_rekognition.types.segment_types_info

        out["selected_segment_types"] = (
            aws_sdk_rekognition.types.segment_types_info.deserialize_aws_json_1_1(
                data["SelectedSegmentTypes"]
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
